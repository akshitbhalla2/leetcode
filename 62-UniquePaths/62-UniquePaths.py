# Last updated: 4/19/2026, 11:23:53 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[0 for j in range(n)] for i in range(m)]

        matrix[0][0] = 1

        for j in range(1, n):
            matrix[0][j] = 1

        for i in range(1, m):
            matrix[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j] 

        return matrix[m-1][n-1] 






