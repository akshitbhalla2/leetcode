# 701. Insert into a Binary Search Tree

**Difficulty:** Medium<br>
[View on LeetCode](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

---

Insert a value that is not already present into a binary search tree, preserving
the BST ordering, and return the root. Any valid resulting tree is accepted.

**Example 1:**

```
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
```

**Example 2:**

```
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

**Constraints:**

- The number of nodes is in `[0, 10^4]`.
- `-10^8 <= Node.val, val <= 10^8`
- Node values are unique, and `val` is not already present.
