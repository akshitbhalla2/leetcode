# Last updated: 4/19/2026, 11:23:56 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        size = len(intervals)

        results = []

        prevStart, prevEnd = intervals[0]
        for start, end in intervals[1:]:
            if start <= prevEnd:
                prevEnd = max(prevEnd, end)
            else:
                results.append([prevStart, prevEnd])
                prevStart, prevEnd = start, end

        results.append([prevStart, prevEnd])

        return results



                