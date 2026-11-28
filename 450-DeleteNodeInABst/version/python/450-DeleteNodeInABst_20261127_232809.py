# Last updated: 11/27/2026, 11:28:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # 0 or 1 child (leaf nodes): return the other side
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # 2 children: replace with inorder successor (min of right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            # replace with min of right subtree
            root.val = successor.val
            # delete min of right subtree (left node)
            root.right = self.deleteNode(root.right, successor.val)

        return root
