# Last updated: 11/28/2026, 1:31:42 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if len(result) < k:
                result.append(node.val)

            inorder(node.right)

        inorder(root)

        for _ in range(k-1):
            heapq.heappop(result)

        return result[0]