# Last updated: 4/19/2026, 11:23:17 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0, n-1

        while left < right:

            mid = (left + right) // 2

            if isBadVersion(mid + 1):
                right = mid

            else:
                left = mid + 1

        return left + 1

        