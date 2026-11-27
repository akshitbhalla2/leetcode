# Last updated: 11/27/2026, 3:38:38 AM
1import math
2
3class Solution:
4    def minEatingSpeed(self, piles: list[int], h: int) -> int:
5
6        lt = 1
7        rt = max(piles)
8
9        while lt <= rt:
10            mid = (lt + rt) // 2
11
12            total = 0
13            for pile in piles:
14                total += math.ceil(pile / mid)
15
16            if total <= h:
17                rt = mid - 1
18            else:
19                lt = mid + 1
20
21        return lt