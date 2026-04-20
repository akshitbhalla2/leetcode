# Last updated: 4/19/2026, 11:23:11 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 0, n-1

        while left <= right:

            mid = (left + right) // 2
            pick = mid + 1
            
            result = guess(pick)

            if result == 0:
                return pick

            elif result == 1:
                left = mid + 1

            else:
                right = mid - 1

        



