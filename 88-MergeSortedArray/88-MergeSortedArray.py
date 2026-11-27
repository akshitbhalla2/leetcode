# Last updated: 11/26/2026, 5:53:58 PM
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums1:
            return nums2

        if not nums2:
            return nums1

        lt, rt = m - 1, n - 1
        for cr in range(m + n - 1, -1, -1):
            if rt < 0:
                break

            if (lt >= 0) and (nums1[lt] >= nums2[rt]):
                nums1[cr] = nums1[lt]
                lt -= 1
            else:
                nums1[cr] = nums2[rt]
                rt -= 1