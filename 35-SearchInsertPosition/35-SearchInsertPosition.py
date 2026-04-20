# Last updated: 4/19/2026, 11:24:02 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binarySearch(nums, left, right, target):
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if left == right:
                if nums[mid] > target:
                    return left
                else:
                    return left + 1

            if left == right + 1:
                return left

            # if nums[mid] == nums[-1]:
            #     return mid + 1

            # if nums[mid] == nums[0]:
            #     return mid + 1
            
            if nums[mid] > target:
                return binarySearch(nums, left, mid - 1, target)

            if nums[mid] < target:
                return binarySearch(nums, mid + 1, right, target)

        return binarySearch(nums, 0, len(nums) - 1, target)

        