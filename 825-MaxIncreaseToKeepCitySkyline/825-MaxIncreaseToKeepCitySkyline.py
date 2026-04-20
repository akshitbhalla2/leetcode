# Last updated: 4/20/2026, 1:17:49 AM
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        import numpy as np

        t = np.array(grid)

        row_max = t.max(axis=1).reshape(-1, 1)
        col_max = t.max(axis=0).reshape(1, -1)
        
        result = np.minimum(row_max, col_max)

        return (result - t).sum()