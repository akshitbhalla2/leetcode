# Last updated: 4/19/2026, 11:23:46 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i = 0
        j = 0

        while j < n:
            nums1[m+j] = nums2[j]
            j += 1

        nums1.sort()