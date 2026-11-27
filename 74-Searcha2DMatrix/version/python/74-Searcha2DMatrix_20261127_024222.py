# Last updated: 11/27/2026, 2:42:22 AM
1class Solution:
2    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
3
4        rows = len(matrix)
5        cols = len(matrix[0])
6        
7        n = rows * cols
8        lt = 0
9        rt = n - 1
10
11        while lt <= rt:
12            mid = (lt + rt) // 2
13
14            i = mid // cols
15            j = mid % cols
16
17            if matrix[i][j] == target:
18                return True
19
20            elif matrix[i][j] < target:
21                lt = mid + 1
22            
23            else:
24                rt = mid - 1
25
26        return False
27
28
29
30        