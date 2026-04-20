# Last updated: 4/19/2026, 11:23:25 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        graph = {}
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    graph[(r, c)] = []
        
        for r in range(rows):
            for c in range(1, columns):
                if (grid[r][c-1] == "1") and (grid[r][c] == "1"):
                    graph[(r, c-1)].append((r, c))
                    graph[(r, c)].append((r, c-1))

        for r in range(1, rows):
            for c in range(columns):
                if (grid[r-1][c] == "1") and (grid[r][c] == "1"):
                    graph[(r-1, c)].append((r, c))
                    graph[(r, c)].append((r-1, c))
            
        def dfs(graph, node):

            visited = set()

            def explore(graph, node):
                
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        explore(graph, neighbor)

            explore(graph, node)
            
            return visited

        count = 0
        visited_all = set()
        for node in graph:
            if node not in visited_all:
                count += 1
                visited = dfs(graph, node)
                visited_all = visited_all.union(visited)

        return count

        