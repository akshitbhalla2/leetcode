# Last updated: 11/26/2026, 11:39:50 PM
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        cr = 0
        lt = 0
        rt = len(nums) - 1

        while cr <= rt:
            if nums[cr] == 0:
                nums[lt], nums[cr] = nums[cr], nums[lt]
                lt += 1
                cr += 1
            elif nums[cr] == 1:
                cr += 1
            else:
                nums[cr], nums[rt] = nums[rt], nums[cr]
                rt -= 1
