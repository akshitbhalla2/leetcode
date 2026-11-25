# Contributing solutions

Use one top-level folder per LeetCode problem, named with its official problem
number and title (for example, `1299-ReplaceElementsWithGreatestElementOnRightSide`).
Keep alternate submissions in that problem's `version/` folder instead of
creating another top-level folder for the same problem. Timestamp-based
`problem-<number>` folders are placeholders and must be resolved to a real
problem before syncing.

Each problem folder should have a `README.md` with the matching numbered title,
the canonical LeetCode problem link, and a concise original summary. Use the
official LeetCode page for the full statement rather than copying it into this
repository.

Run `python tools/validate_problem_sync.py` before syncing. The GitHub Actions
check validates changed problem folders and rejects missing or mismatched
problem references, as well as duplicate LeetCode links. Configure this check
as required in branch protection if sync changes should be blocked from merging.
