# Last updated: 4/19/2026, 11:23:36 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        size = len(nums)

        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]

        for i in range(1, size):

            if nums[i] < 0:
                min_prod, max_prod = max_prod, min_prod
            
            max_prod = max(nums[i], nums[i] * max_prod)
            min_prod = min(nums[i], nums[i] * min_prod)

            result = max(result, max_prod)

        return result