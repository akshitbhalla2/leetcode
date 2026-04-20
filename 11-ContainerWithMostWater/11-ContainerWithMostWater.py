# Last updated: 4/19/2026, 11:24:10 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:

        size = len(height)

        max_area = 0
        left = 0
        right = size-1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area) 

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        