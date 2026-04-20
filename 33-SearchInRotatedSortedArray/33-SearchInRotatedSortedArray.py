# Last updated: 4/19/2026, 11:24:02 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        size = len(nums)
        left = 0
        right = size-1

        while left < right:

            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        start = left

        if (target >= nums[start]) and (target <= nums[size-1]):
            left = start
            right = size-1 
        elif (target >= nums[0]) and (target <= nums[start-1]):
            left = 0
            right = start-1
        else:
            return -1
        
        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            elif left == right:
                return -1

            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid

        return left

        


        