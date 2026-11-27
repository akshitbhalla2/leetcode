# Last updated: 11/16/2026, 12:02:39 AM
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2

        nums = [0] * n
        nums[0] = 1
        nums[1] = 2
        for i in range(2, n):
            nums[i] = nums[i-1] + nums[i-2]

        return nums[-1]
