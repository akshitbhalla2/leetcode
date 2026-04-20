# Last updated: 4/19/2026, 11:23:58 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        size = len(nums)

        total = 0
        maximum = -float("inf")

        for i in range(0, size):
            total += nums[i]
            
            maximum = max(maximum, total)
            total = max(0, total)


        return maximum





