# Last updated: 4/20/2026, 12:00:33 AM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, _ in enumerate(nums):
            if nums[i] == val:
                continue
            nums[k] = nums[i]
            k += 1
        return k














        # size = len(nums)

        # i = 0
        # for j in range(size):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i += 1

        # return i
