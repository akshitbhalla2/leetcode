# Last updated: 11/16/2026, 12:02:39 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        if n == 1:
5            return 1
6        
7        if n == 2:
8            return 2
9
10        nums = [0] * n
11        nums[0] = 1
12        nums[1] = 2
13        for i in range(2, n):
14            nums[i] = nums[i-1] + nums[i-2]
15        
16        return nums[-1] 
17
18        