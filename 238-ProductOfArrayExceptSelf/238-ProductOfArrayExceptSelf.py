# Last updated: 4/19/2026, 11:23:19 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)

        prod = 1

        count = 0
        for i in range(size):
            if nums[i] == 0:
                count += 1
            else:
                prod *= nums[i]


        results = [0] * size

        if count > 1:
            return results

        elif count == 1:
            for i in range(size):
                if nums[i] == 0:
                    results[i] = prod

        else: 
            for i in range(size):
                results[i] = int(prod / nums[i])

        return results
        