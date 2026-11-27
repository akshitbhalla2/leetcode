# Contributing solutions

Use one top-level folder per LeetCode problem, named with its official problem
number and title (for example, `1299-ReplaceElementsWithGreatestElementOnRightSide`).
Keep the latest solution for each language at the problem-folder root and move
older attempts into that problem's `version/` folder. Do not create another
top-level folder for the same problem. Timestamp-based `problem-<number>`
folders are placeholders and must be resolved to a real problem before syncing.

Every `README.md`, including ones under `version/`, should use the same
structure:

```markdown
# <number>. <problem title>

**Difficulty:** <Easy|Medium|Hard><br>
[View on LeetCode](https://leetcode.com/problems/<problem-slug>/)

---

<problem statement or concise summary>
```

Each problem folder must have a root `README.md` with the matching numbered
title and canonical LeetCode link. Use the official LeetCode page for the full
statement rather than copying it into this repository.

Run `python tools/validate_problem_sync.py` before syncing. The GitHub Actions
check validates changed problem folders and rejects missing or mismatched
problem references, as well as duplicate LeetCode links. Configure this check
as required in branch protection if sync changes should be blocked from merging.
