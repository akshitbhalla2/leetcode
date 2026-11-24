# Last updated: 4/19/2026, 11:22:09 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # return nums + nums

        size = len(nums)
        
        ans = [0] * (2 * size)

        for i in range(size):
            ans[i] = nums[i]
            ans[i + size] = nums[i] 

        return ans