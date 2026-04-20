# Last updated: 4/19/2026, 11:24:05 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        size = len(nums)

        if size < 2:
            return size

        i = 0
        j = 1

        while j < size:
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]

        return i+1