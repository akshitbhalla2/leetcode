# Last updated: 11/13/2026, 2:13:03 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        max_ = -float("inf")
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                counter = 0

            max_ = max(max_, counter)

        return max_
