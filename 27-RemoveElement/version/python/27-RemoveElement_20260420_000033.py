# Last updated: 4/20/2026, 12:00:33 AM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4        for i, _ in enumerate(nums):
5            if nums[i] == val:
6                continue
7            nums[k] = nums[i]
8            k += 1
9        return k
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24        # size = len(nums)
25
26        # i = 0
27        # for j in range(size):
28        #     if nums[j] != val:
29        #         nums[i] = nums[j]
30        #         i += 1
31
32        # return i
33
34        