# Last updated: 11/28/2026, 12:00:26 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:

        # inorder    : left, root, right
        # pre-order  : root, left, right
        # post-order : left, right, root

        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)

        return result
