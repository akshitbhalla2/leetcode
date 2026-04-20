# Last updated: 4/19/2026, 11:23:13 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # from collections import Counter

        # result =  Counter(nums).most_common(k)

        # return [r[0] for r in result]

        size = len(nums)

        counter = {}
        for i in range(size):
            c = nums[i]
            counter[c] = 1 + counter.get(c, 0) 

        result = []
        for c in counter:
            result.append((c, counter[c]))

        result.sort(key=lambda tup: -tup[1])

        return [r[0] for r in result[:k]]

