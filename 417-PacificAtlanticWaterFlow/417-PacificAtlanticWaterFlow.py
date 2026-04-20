# Last updated: 4/19/2026, 11:23:10 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        graph = {}

        graph["P"] = [(0, 0)]
        graph["A"] = [(m-1, n-1)]

        for i in range(m):
            for j in range(n):
                graph[(i, j)] = []

        for i in range(1, m):
            graph["P"].append((i, 0))

        for i in range(0, m-1):
            graph["A"].append((i, n-1))
    
        for j in range(1, n):
            graph["P"].append((0, j))

        for j in range(0, n-1):
            graph["A"].append((m-1, j))

        for i in range(0, m):
            for j in range(1, n):
                if heights[i][j-1] < heights[i][j]:
                    graph[(i, j-1)].append((i, j))
                elif heights[i][j-1] > heights[i][j]:
                    graph[(i, j)].append((i, j-1))
                else:
                    graph[(i, j-1)].append((i, j))
                    graph[(i, j)].append((i, j-1))

        for i in range(1, m):
            for j in range(0, n):
                if heights[i-1][j] < heights[i][j]:
                    graph[(i-1, j)].append((i, j))
                elif heights[i-1][j] > heights[i][j]:
                    graph[(i, j)].append((i-1, j))
                else:
                    graph[(i-1, j)].append((i, j))
                    graph[(i, j)].append((i-1, j))

        def dfs(graph, start):

            visited = set()

            def explore(node):
                visited.add(node)           
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        explore(neighbor)

            explore(start)
            
            return visited


        p_reachable = dfs(graph, "P")
        a_reachable = dfs(graph, "A")

        return p_reachable.intersection(a_reachable)



