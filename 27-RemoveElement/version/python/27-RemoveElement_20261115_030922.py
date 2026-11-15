# Last updated: 11/15/2026, 3:09:22 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4        for num in nums:
5            if num != val:
6                nums[k] = num
7                k += 1
8        return k
9
10        