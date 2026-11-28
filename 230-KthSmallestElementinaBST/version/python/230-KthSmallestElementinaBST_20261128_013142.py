# Last updated: 11/28/2026, 1:31:42 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
9
10        result = []
11
12        def inorder(node):
13            if not node:
14                return 
15
16            inorder(node.left)
17        
18            if len(result) < k:
19                result.append(node.val)
20
21            inorder(node.right)
22
23        inorder(root)
24
25        for _ in range(k-1):
26            heapq.heappop(result)
27        
28        return result[0]
29
30            
31
32            