# Last updated: 4/19/2026, 11:23:40 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        # nums = list(set(nums))
        # nums.sort()

        # maxs = [1]
        # count = 1

        # for i in range(1, len(nums)):
            
        #     if (nums[i] == nums[i-1] + 1):
        #         count += 1
        #     else:
        #         count = 1

        #     maxs.append(count)        

        # return max(maxs)

        nums.sort()

        maxs = [1]
        count = 1

        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1] + 1:
                count += 1

            elif nums[i] == nums[i-1]:
                count += 0

            else:
                count = 1

            maxs.append(count)        

        return max(maxs)