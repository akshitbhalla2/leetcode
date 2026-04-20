# Last updated: 4/19/2026, 11:23:09 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        count = 0
        prevStart, prevEnd = intervals[0]
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)

        return count









