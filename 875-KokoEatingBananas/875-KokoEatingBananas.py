# Last updated: 11/27/2026, 3:38:38 AM
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lt = 1
        rt = max(piles)

        while lt <= rt:
            mid = (lt + rt) // 2

            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)

            if total <= h:
                rt = mid - 1
            else:
                lt = mid + 1

        return lt
        