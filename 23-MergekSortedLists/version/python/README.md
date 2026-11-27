# 23. Merge k Sorted Lists

**Difficulty:** Hard<br>
[View on LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)

---

Merge `k` sorted linked lists into a single sorted linked list and return its
head. The result should contain all nodes in ascending order.

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- The sum of all list lengths does not exceed `10^4`.
