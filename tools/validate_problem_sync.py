import argparse
from datetime import datetime
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEM_FOLDER = re.compile(r"^(\d+)-(.+)$")
PLACEHOLDER_FOLDER = re.compile(r"^problem-\d+$", re.IGNORECASE)
HEADING = re.compile(r"^#\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
DIFFICULTY = re.compile(
    r"^\*\*Difficulty:\*\*\s+(Easy|Medium|Hard)(?:<br>)?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
PROBLEM_URL = re.compile(
    r"https?://leetcode\.com/problems/([a-z0-9-]+)/?", re.IGNORECASE
)
SECTION_DIVIDER = re.compile(r"^---\s*$", re.MULTILINE)
UPDATED_AT = re.compile(
    r"Last updated:\s*(\d{1,2}/\d{1,2}/\d{4}),\s*(\d{1,2}:\d{2}:\d{2}\s*[AP]M)",
    re.IGNORECASE,
)
TIMESTAMPED_FILENAME = re.compile(r"_(\d{8}_\d{6})\.[^.]+$")
NUMBERED_SOURCE_LINE = re.compile(r"^\d+")


def git_output(*args):
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def changed_paths(base):
    if base:
        if set(base) == {"0"}:
            base = "HEAD~1"
        return git_output("diff", "--name-only", base, "HEAD").splitlines()
    paths = set(git_output("diff", "--name-only", "HEAD").splitlines())
    paths.update(git_output("ls-files", "--others", "--exclude-standard").splitlines())
    return sorted(paths)


def normalized(value):
    return re.sub(r"[^a-z0-9]", "", value.lower())


def validate_readme(readme, problem_id, folder_title=None):
    errors = []
    content = readme.read_text(encoding="utf-8")
    label = readme.as_posix()
    heading = HEADING.search(content)

    if not heading:
        errors.append(f"{label}: needs a '# <id>. <title>' heading")
    else:
        heading_id, heading_title = heading.groups()
        if heading_id != problem_id:
            errors.append(f"{label}: heading uses problem {heading_id}, expected {problem_id}")
        if folder_title and normalized(heading_title) != normalized(folder_title):
            errors.append(f"{label}: title does not match the problem folder")

    problem_url = PROBLEM_URL.search(content)
    if not problem_url:
        errors.append(f"{label}: needs a canonical LeetCode problem link")
    elif heading:
        title_slug = re.sub(r"[^a-z0-9\s-]", "", heading.group(2).lower())
        title_slug = re.sub(r"\s+", "-", title_slug.strip())
        if title_slug != problem_url.group(1).lower():
            errors.append(f"{label}: LeetCode link does not match the README title")

    if not DIFFICULTY.search(content):
        errors.append(f"{label}: needs a '**Difficulty:** <level>' line")
    if not SECTION_DIVIDER.search(content):
        errors.append(f"{label}: needs a '---' divider after the metadata")
    return errors


def validate_problem_folder(folder):
    errors = []
    for source in folder.rglob("*.py"):
        for line_number, line in enumerate(
            source.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if NUMBERED_SOURCE_LINE.match(line):
                errors.append(
                    f"{source.relative_to(folder)}:{line_number}: "
                    "remove the literal line-number prefix"
                )

    folder_match = PROBLEM_FOLDER.match(folder.name)
    if not folder_match:
        return errors

    problem_id, folder_title = folder_match.groups()
    readme = folder / "README.md"
    if not readme.is_file():
        errors.append(f"{folder.name}: missing README.md with a problem reference")

    errors.extend(validate_latest_solution_is_primary(folder))
    for path in folder.rglob("README.md"):
        errors.extend(
            validate_readme(
                path,
                problem_id,
                folder_title if path == readme else None,
            )
        )
    return errors


def solution_timestamp(path):
    content = path.read_text(encoding="utf-8")
    updated = UPDATED_AT.search(content)
    if updated:
        return datetime.strptime(
            " ".join(updated.groups()), "%m/%d/%Y %I:%M:%S %p"
        )

    filename_timestamp = TIMESTAMPED_FILENAME.search(path.name)
    if filename_timestamp:
        return datetime.strptime(filename_timestamp.group(1), "%Y%m%d_%H%M%S")

    committed_at = git_output(
        "log", "-1", "--format=%cI", "--", str(path.relative_to(ROOT))
    ).strip()
    if committed_at:
        return datetime.fromisoformat(committed_at).replace(tzinfo=None)
    return None


def validate_latest_solution_is_primary(folder):
    version_dir = folder / "version"
    if not version_dir.is_dir():
        return []

    errors = []
    root_solutions = [
        path
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in {".py", ".sql"}
    ]
    archived_solutions = [
        path
        for path in version_dir.rglob("*")
        if path.is_file() and path.suffix.lower() in {".py", ".sql"}
    ]
    root_extensions = {path.suffix.lower() for path in root_solutions}
    for extension in sorted(
        {path.suffix.lower() for path in archived_solutions} - root_extensions
    ):
        archived = next(
            path for path in archived_solutions if path.suffix.lower() == extension
        )
        errors.append(
            f"{folder.name}: missing top-level {extension} solution for "
            f"archived {archived.relative_to(folder)}"
        )

    for root_solution in root_solutions:
        archived = [
            path
            for path in archived_solutions
            if path.suffix.lower() == root_solution.suffix.lower()
        ]
        dated_archived = [
            (solution_timestamp(path), path)
            for path in archived
            if solution_timestamp(path) is not None
        ]
        if not dated_archived:
            continue

        latest_timestamp, latest_path = max(dated_archived, key=lambda item: item[0])
        root_timestamp = solution_timestamp(root_solution)
        if root_timestamp is None or latest_timestamp > root_timestamp:
            errors.append(
                f"{folder.name}: promote newer {latest_path.relative_to(folder)} "
                f"over {root_solution.name}"
            )
    return errors


def validate_unique_links():
    errors = []
    linked_folders = {}
    for folder in ROOT.iterdir():
        if not folder.is_dir() or not PROBLEM_FOLDER.match(folder.name):
            continue
        readme = folder / "README.md"
        if not readme.is_file():
            continue
        content = readme.read_text(encoding="utf-8")
        for match in PROBLEM_URL.finditer(content):
            slug = match.group(1).lower()
            previous = linked_folders.get(slug)
            if previous and previous != folder.name:
                errors.append(
                    f"{folder.name}: duplicates LeetCode problem link used by {previous}"
                )
            linked_folders[slug] = folder.name
    return errors


def validate_unique_folder_names():
    paths = git_output("ls-files", "-z").split("\0")
    paths.extend(
        git_output("ls-files", "--others", "--exclude-standard", "-z").split("\0")
    )
    names = {
        path.split("/", 1)[0]
        for path in paths
        if path and Path(path.split("/", 1)[0]).is_dir()
    }

    errors = []
    for name in sorted(names):
        if PLACEHOLDER_FOLDER.match(name):
            errors.append(
                f"{name}: placeholder problem folder; use the numeric LeetCode ID and title"
            )

    problem_names = {name for name in names if PROBLEM_FOLDER.match(name)}
    seen = {}
    for name in sorted(problem_names):
        key = name.casefold()
        previous = seen.get(key)
        if previous and previous != name:
            errors.append(
                f"{name}: case-insensitive duplicate of problem folder {previous}"
            )
        else:
            seen[key] = name
    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate changed LeetCode problem folders and problem references."
    )
    parser.add_argument(
        "--base",
        help="Base git revision to compare with HEAD (used by GitHub Actions).",
    )
    args = parser.parse_args()

    changed_folders = set()
    for path in changed_paths(args.base):
        parts = Path(path).parts
        if parts and PROBLEM_FOLDER.match(parts[0]):
            changed_folders.add(parts[0])

    folders_to_validate = [
        ROOT / name
        for name in sorted(changed_folders)
        if (ROOT / name).is_dir()
    ]
    errors = []
    for folder in folders_to_validate:
        errors.extend(validate_problem_folder(folder))
    errors.extend(validate_unique_links())
    errors.extend(validate_unique_folder_names())

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(folders_to_validate)} changed problem folder(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
