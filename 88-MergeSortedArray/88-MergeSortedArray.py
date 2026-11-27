# Last updated: 11/26/2026, 5:53:58 PM
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        lt, rt = m - 1, n - 1
        for cr in range(m + n - 1, -1, -1):
            a = nums1[lt] if lt >= 0 else -float("inf")
            b = nums2[rt] if rt >= 0 else -float("inf")

            if a >= b:
                nums1[cr] = a
                lt -= 1
            else:
                nums1[cr] = b
                rt -= 1