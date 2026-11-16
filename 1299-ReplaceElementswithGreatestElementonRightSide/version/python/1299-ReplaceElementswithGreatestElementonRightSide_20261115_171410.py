# Last updated: 11/15/2026, 5:14:10 PM
1class Solution:
2    def replaceElements(self, arr: List[int]) -> List[int]:
3        # l = len(arr)
4        # max_ = arr[-1]
5        # for i in range(l-2, -1, -1):
6        #     v = arr[i]
7        #     arr[i] = max_
8        #     max_ = max(max_, v)   
9        # arr[-1] = -1
10        # return arr
11
12        size = len(arr)
13        max_ = -float("inf")
14        prev = arr[-1]
15        arr[-1] = -1
16        for i in range(size-2, -1, -1):
17            curr = arr[i]
18            max_ = max(max_, prev)
19            arr[i] = max_
20            prev = curr
21        return arr
22
23
24        