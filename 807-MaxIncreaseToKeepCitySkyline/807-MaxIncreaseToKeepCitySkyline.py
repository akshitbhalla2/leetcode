# Last updated: 11/15/2026, 5:22:00 PM
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        import numpy as np

        t = np.array(grid)

        row_max = t.max(axis=1).reshape(-1, 1)
        col_max = t.max(axis=0).reshape(1, -1)
        
        result = np.minimum(row_max, col_max)

        return (result - t).sum()