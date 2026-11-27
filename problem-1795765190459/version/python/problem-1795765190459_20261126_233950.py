# Last updated: 11/26/2026, 11:39:50 PM
1class Solution:
2    def sortColors(self, nums: list[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        
7        cr = 0
8        lt = 0
9        rt = len(nums) - 1
10
11        while cr <= rt:
12            if nums[cr] == 0:
13                nums[lt], nums[cr] = nums[cr], nums[lt]
14                lt += 1
15                cr += 1
16            elif nums[cr] == 1:
17                cr += 1
18            else:
19                nums[cr], nums[rt] = nums[rt], nums[cr]
20                rt -= 1