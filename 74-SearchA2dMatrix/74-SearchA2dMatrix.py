# Last updated: 4/19/2026, 11:23:49 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows*cols - 1

        while left <= right:

            mid = (left + right) // 2

            i = mid // cols 
            j = mid % cols

            if matrix[i][j] == target:
                return True

            elif matrix[i][j] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        