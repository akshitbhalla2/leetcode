# Last updated: 11/26/2026, 9:40:43 PM
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        # points = sorted(points, key=lambda p: (p[0]**2 + p[1]**2)**0.5)
        # return points[:k]

        heap = []
        for x, y in points:
            dist = (x**2 + y**2)**0.5
            heapq.heappush(heap, (-dist, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]
