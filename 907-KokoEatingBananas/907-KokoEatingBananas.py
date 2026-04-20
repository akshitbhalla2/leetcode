# Last updated: 4/19/2026, 11:22:29 PM
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def cocoFinish(piles, h, k):
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k) 
            
            return hours <= h

        left, right = 0, max(piles) - 1

        while left < right:

            mid = (left + right) // 2
            k = mid + 1

            if cocoFinish(piles, h, k):
                right = mid 
            else:
                left = mid + 1 

        return left + 1
        