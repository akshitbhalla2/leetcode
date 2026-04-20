# Last updated: 4/19/2026, 11:23:56 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # size = len(nums)

        # graph = {}
        # for i in range(size):
        #     graph[i] = [i+1+j for j in range(nums[i]) if i+1+j < size]

        # def dfs(start):

        #     visited = set()

        #     def explore(node):
        #         visited.add(node)
        #         for neighbor in graph[node]:
        #             if neighbor not in visited:
        #                 explore(neighbor)
            
        #     explore(start)

        #     return visited
        
        # reachable_nodes = dfs(0)

        # if (size-1) in reachable_nodes:
        #     return True
        
        # return False

        size = len(nums)

        farthest = 0
        for i in range(size):
            
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if farthest >= size - 1:
                return True 

        return False



