# Last updated: 4/19/2026, 11:24:13 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_dict = {}
        for i, num1 in enumerate(nums):
            num2 = target - num1

            if num2 in nums_dict:
                return [nums_dict[num2], i] 

            nums_dict[num1] = i
                
        