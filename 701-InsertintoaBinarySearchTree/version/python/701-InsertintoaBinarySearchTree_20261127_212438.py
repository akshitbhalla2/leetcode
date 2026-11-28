# Last updated: 11/27/2026, 9:24:38 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
9
10        if not root:
11            return TreeNode(val)
12        
13        if val < root.val:
14            root.left = self.insertIntoBST(root.left, val)
15        elif val > root.val:
16            root.right = self.insertIntoBST(root.right, val)
17        
18        return root
19        