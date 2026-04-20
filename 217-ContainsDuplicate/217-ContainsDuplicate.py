# Last updated: 4/19/2026, 11:23:22 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        from collections import Counter

        freq = Counter(nums)

        if len(freq) == len(nums):
            return False

        return True