# Last updated: 11/28/2026, 12:00:26 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
9
10        # inorder    : left, root, right
11        # pre-order  : root, left, right
12        # post-order : left, right, root
13
14        result = []
15        
16        def traverse(node):
17            if not node:
18                return
19            
20            traverse(node.left)
21            result.append(node.val)
22            traverse(node.right)
23        
24        traverse(root)
25
26        return result