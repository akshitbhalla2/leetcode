# Last updated: 4/19/2026, 11:23:15 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        size = len(nums)

        dp = [1] * size

        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)