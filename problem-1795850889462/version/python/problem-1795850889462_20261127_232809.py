# Last updated: 11/27/2026, 11:28:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
9
10        if not root:
11            return None
12
13        if key < root.val:
14            root.left = self.deleteNode(root.left, key)
15        elif key > root.val:
16            root.right = self.deleteNode(root.right, key)
17        else:
18            # 0 or 1 child (leaf nodes): return the other side
19            if not root.left:
20                return root.right
21            
22            if not root.right:
23                return root.left
24
25            # 2 children: replace with inorder successor (min of right subtree)
26            successor = root.right
27            while successor.left:
28                successor = successor.left
29            
30            # replace with min of right subtree
31            root.val = successor.val
32            # delete min of right subtree (left node)
33            root.right = self.deleteNode(root.right, successor.val)
34
35        return root