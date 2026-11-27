# Last updated: 11/26/2026, 5:49:37 PM
1class Solution:
2    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6
7        if not nums1:
8            return nums2
9        
10        if not nums2:
11            return nums1
12
13        lt, rt = m - 1, n - 1
14        for cr in range(m + n - 1, -1, -1):
15            if rt < 0:
16                break
17
18            if (lt >= 0) and (nums1[lt] >= nums2[rt]):
19                nums1[cr] = nums1[lt]
20                lt -= 1
21            else:
22                nums1[cr] = nums2[rt]
23                rt -= 1