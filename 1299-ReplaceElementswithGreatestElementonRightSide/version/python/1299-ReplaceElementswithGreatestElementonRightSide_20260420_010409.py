# Last updated: 4/20/2026, 1:04:09 AM
1class Solution:
2    def replaceElements(self, arr: List[int]) -> List[int]:
3        size = len(arr)
4        m = float('-inf')
5        maxes = []
6        for i in range(size-1, 0, -1):
7            m = max(m, arr[i])
8            maxes.insert(0, m)
9        maxes.append(-1)
10        return maxes
11
12        #     cur = arr[i]
13        #     nex = arr[i+1]
14        #     m = max(nex, m)
15        #     arr[i] = m
16        # arr[-1] = -1
17        # return arr