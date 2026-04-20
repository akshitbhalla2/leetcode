# Last updated: 4/19/2026, 11:23:23 PM
class Solution:
    def rob(self, nums: List[int]) -> int:

        size = len(nums)

        if size == 1:
            return nums[0]

        def rob(nums):
            
            size = len(nums)

            if size == 1:
                return nums[0]

            if size == 2:
                return max(nums)

            if size == 3:
                return max(nums[0] + nums[2], nums[1])
            
            dp = [0] * size
            
            for i in range(2):
                dp[i] = nums[i]
                    
            dp[2] = dp[0] + nums[2]
            
            for i in range(3, size):
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
                
            return max(dp)

        return max(rob(nums[:-1]), rob(nums[1:]))

        