# Last updated: 11/15/2026, 5:29:48 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        
4        # # return nums + nums
5
6        # size = len(nums)
7        # ans = [0] * size * 2
8        # for i in range(size):
9        #     ans[i] = nums[i] 
10        #     ans[i + size] = nums[i]
11        # return ans   
12
13        size = len(nums)
14        for i in range(size):
15            nums.append(nums[i])
16        return nums
17
18        