# Last updated: 4/19/2026, 11:23:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def traverse(node):
            if not node:
                return []

            return traverse(node.left) + [node.val] + traverse(node.right)

        sorted_nums = traverse(root)

        return sorted_nums[k-1]
        