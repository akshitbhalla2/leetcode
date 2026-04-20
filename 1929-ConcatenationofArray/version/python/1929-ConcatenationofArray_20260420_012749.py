# Last updated: 4/20/2026, 1:27:49 AM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        
4        return nums + nums
5
6
7
8
9
10
11
12
13
14
15        # size = len(nums)
16        
17        # ans = [0] * (2 * size)
18
19        # for i in range(size):
20        #     ans[i] = nums[i]
21        #     ans[i + size] = nums[i] 
22
23        # return ans