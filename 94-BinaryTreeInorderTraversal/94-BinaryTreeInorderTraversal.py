# Last updated: 4/19/2026, 11:23:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        # results = []

        # def traverse(node):
        #     if node:
        #         traverse(node.left)
        #         results.append(node.val)
        #         traverse(node.right)
        
        # traverse(root)

        # return results
        