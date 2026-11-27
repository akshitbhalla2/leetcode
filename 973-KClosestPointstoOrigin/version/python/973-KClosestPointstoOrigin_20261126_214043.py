# Last updated: 11/26/2026, 9:40:43 PM
1class Solution:
2    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
3        points = sorted(points, key=lambda p: (p[0]**2 + p[1]**2)**0.5)
4        return points[:k]