# Last updated: 4/19/2026, 11:23:24 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            graph[p].append(c)

        visited = set()
        stack = set()

        # Cycle detection
        def explore(node):

            if node in stack:
                return False

            if node in visited:
                return True

            stack.add(node)

            for neighbor in graph[node]:
                if not explore(neighbor):
                    return False

            stack.remove(node)
            visited.add(node)

            return True

        for i in range(numCourses):
            # If cycle does not exist then courses can be completed
            if not explore(i):
                return False
        
        return True