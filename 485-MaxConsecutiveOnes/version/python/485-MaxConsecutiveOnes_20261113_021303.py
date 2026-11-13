# Last updated: 11/13/2026, 2:13:03 AM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3
4        max_ = -float("inf")
5        counter = 0
6        for num in nums:
7            if num == 1:            
8                counter += 1
9            else:
10                counter = 0
11
12            max_ = max(max_, counter)
13
14        return max_
15        