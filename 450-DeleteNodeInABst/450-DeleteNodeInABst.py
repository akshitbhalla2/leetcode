# Last updated: 4/19/2026, 11:23:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return 

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else: # Found the node to delete
            if not root.left: # Only right child or no child
                return root.right
            if not root.right: # Only left child
                return root.left    

            # Node must have two children
            # Find the smallest node in the right subtree (inorder successor).
            # Replace the current node's value with that of the successor.
            # Recursively delete the successor.

            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root

            