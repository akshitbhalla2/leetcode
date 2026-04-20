# Last updated: 4/19/2026, 11:23:39 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        from collections import Counter

        nums_dict = Counter(nums)

        for k in nums_dict:
            if nums_dict[k] == 1:
                return k
        