# Last updated: 11/26/2026, 11:59:11 PM
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lt, rt = 0, len(nums) - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lt = mid + 1
            else:
                rt = mid - 1

        return -1
