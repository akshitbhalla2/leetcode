# Last updated: 11/27/2026, 3:01:10 AM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lt = 1
        rt = n

        while lt <= rt:
            mid = (lt + rt) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                lt = mid + 1
            else:
                rt = mid - 1

        return -1
