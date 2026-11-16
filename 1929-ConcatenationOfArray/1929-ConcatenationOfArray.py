# Last updated: 11/15/2026, 5:20:55 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # return nums + nums

        size = len(nums)
        ans = [0] * size * 2
        for i in range(size):
            ans[i] = nums[i] 
            ans[i + size] = nums[i]
        return ans   