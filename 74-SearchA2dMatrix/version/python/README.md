# 74. Search a 2D Matrix

**Difficulty:** Medium<br>
[View on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/)

---

Search a matrix whose rows are sorted and whose first value in each row is
greater than the last value in the previous row. Return whether the target is
present. The search must run in `O(log(m * n))` time.

**Example 1:**

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

**Example 2:**

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`
