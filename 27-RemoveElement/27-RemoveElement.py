# Last updated: 4/19/2026, 11:24:04 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        size = len(nums)

        i = 0
        for j in range(size):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

        