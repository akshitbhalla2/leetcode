# Last updated: 11/28/2026, 1:16:38 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: TreeNode | None) -> bool:
9        
10        def height(node):
11
12            if not node:
13                return 0
14
15            left = height(node.left)
16            if left == -1:
17                return -1
18
19            right = height(node.right)
20            if right == -1:
21                return -1
22
23            if abs(left - right) > 1:
24                return -1 
25
26            return 1 + max(left, right)
27
28        return height(root) != -1