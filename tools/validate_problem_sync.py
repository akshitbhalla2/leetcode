import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROBLEM_FOLDER = re.compile(r"^(\d+)-(.+)$")
PLACEHOLDER_FOLDER = re.compile(r"^problem-\d+$", re.IGNORECASE)
HEADING = re.compile(r"^#\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
PROBLEM_URL = re.compile(
    r"https?://leetcode\.com/problems/([a-z0-9-]+)/?", re.IGNORECASE
)


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


def validate_problem_folder(folder):
    errors = []
    folder_match = PROBLEM_FOLDER.match(folder.name)
    if not folder_match:
        return errors

    problem_id, folder_title = folder_match.groups()
    readme = folder / "README.md"
    if not readme.is_file():
        return [f"{folder.name}: missing README.md with a problem reference"]

    content = readme.read_text(encoding="utf-8")
    heading = HEADING.search(content)
    if not heading:
        errors.append(f"{folder.name}: README.md needs a '# <id>. <title>' heading")
    else:
        heading_id, heading_title = heading.groups()
        if heading_id != problem_id:
            errors.append(
                f"{folder.name}: README heading uses problem {heading_id}, "
                f"expected {problem_id}"
            )
        if normalized(heading_title) != normalized(folder_title):
            errors.append(
                f"{folder.name}: README title does not match the folder title"
            )

    problem_url = PROBLEM_URL.search(content)
    if not problem_url:
        errors.append(f"{folder.name}: README.md needs a canonical LeetCode problem link")
    elif heading:
        title_slug = re.sub(r"[^a-z0-9\s-]", "", heading.group(2).lower())
        title_slug = re.sub(r"\s+", "-", title_slug.strip())
        if title_slug != problem_url.group(1).lower():
            errors.append(
                f"{folder.name}: LeetCode link does not match the README problem title"
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
        if path
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
