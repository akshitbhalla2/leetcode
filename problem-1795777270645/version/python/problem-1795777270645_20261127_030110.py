# Last updated: 11/27/2026, 3:01:10 AM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        
11        lt = 0
12        rt = n - 1
13
14        while lt <= rt:
15            mid = (lt + rt) // 2
16
17            g = guess(mid)
18
19            if g == 0:
20                return mid
21            elif g == 1:
22                lt = mid + 1
23            else:
24                rt = mid - 1
25
26        return mid + 1