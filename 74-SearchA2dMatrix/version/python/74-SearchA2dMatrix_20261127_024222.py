# Last updated: 11/27/2026, 2:42:22 AM
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        n = rows * cols
        lt = 0
        rt = n - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            i = mid // cols
            j = mid % cols

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lt = mid + 1
            else:
                rt = mid - 1

        return False