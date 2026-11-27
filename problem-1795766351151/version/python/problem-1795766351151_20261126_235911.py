# Last updated: 11/26/2026, 11:59:11 PM
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        
4        lt = 0
5        rt = len(nums) - 1
6
7        while lt <= rt:
8            mid = (lt + rt) // 2
9
10            if nums[mid] == target:
11                return mid
12            elif nums[mid] < target:
13                lt = mid + 1
14            else:
15                rt = mid - 1
16
17        return -1