# Last updated: 4/19/2026, 11:24:07 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # size = len(nums)

        # counts = {}
        # for i in range(size):
        #     if nums[i] in counts:
        #         counts[nums[i]] += 1
        #     else:
        #         counts[nums[i]] = 1

        # results = set()
        # for i in range(0, size-1):
        #     for j in range(i+1, size):
        #         num3 = - (nums[i] + nums[j])

        #         # print(i, nums[i], j, nums[j], num3)

        #         if num3 in counts:
                    
        #             if num3 == nums[i]:
        #                 if counts[num3] > 1:
        #                     if nums[i] >= nums[j] >= num3:
        #                         results.add((nums[i], nums[j], num3))
        #                     elif nums[i] >= num3 >= nums[j]:
        #                         results.add((nums[i], num3, nums[j]))
        #                     elif nums[j] >= nums[i] >= num3:
        #                         results.add((nums[j], nums[i], num3))
        #                     elif nums[j] >= num3 >= nums[i]:
        #                         results.add((nums[j], num3, nums[i]))
        #                     elif num3 >= nums[i] >= nums[j]:
        #                         results.add((num3, nums[i], nums[j]))
        #                     elif num3 >= nums[j] >= nums[i]:
        #                         results.add((num3, nums[j], nums[i]))

        #             elif num3 == nums[j]:
        #                 if counts[num3] > 1:
        #                     if nums[i] >= nums[j] >= num3:
        #                         results.add((nums[i], nums[j], num3))
        #                     elif nums[i] >= num3 >= nums[j]:
        #                         results.add((nums[i], num3, nums[j]))
        #                     elif nums[j] >= nums[i] >= num3:
        #                         results.add((nums[j], nums[i], num3))
        #                     elif nums[j] >= num3 >= nums[i]:
        #                         results.add((nums[j], num3, nums[i]))
        #                     elif num3 >= nums[i] >= nums[j]:
        #                         results.add((num3, nums[i], nums[j]))
        #                     elif num3 >= nums[j] >= nums[i]:
        #                         results.add((num3, nums[j], nums[i]))

        #             else:
        #                 if nums[i] >= nums[j] >= num3:
        #                     results.add((nums[i], nums[j], num3))
        #                 elif nums[i] >= num3 >= nums[j]:
        #                     results.add((nums[i], num3, nums[j]))
        #                 elif nums[j] >= nums[i] >= num3:
        #                     results.add((nums[j], nums[i], num3))
        #                 elif nums[j] >= num3 >= nums[i]:
        #                     results.add((nums[j], num3, nums[i]))
        #                 elif num3 >= nums[i] >= nums[j]:
        #                     results.add((num3, nums[i], nums[j]))
        #                 elif num3 >= nums[j] >= nums[i]:
        #                     results.add((num3, nums[j], nums[i]))

        # res = []
        # for tup in results:
        #     if tup[0] == tup[1] == tup[2] == 0:
        #         if counts[0] < 3:
        #             continue
        #     res.append(list(tup))

        # return res        


        size = len(nums)

        nums.sort()

        results = []
        for i in range(size-2):

            if (i > 0) and (nums[i] == nums[i-1]):
                continue 
            
            l = i + 1
            r = size - 1
            
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r] 

                if threeSum == 0:
                    results.append((nums[i], nums[l], nums[r]))

                if threeSum > 0:
                    while l < r:
                        r -= 1
                        if nums[r] != nums[r+1]:
                            break
                else:
                    while l < r:
                        l += 1
                        if nums[l] != nums[l-1]:
                            break

        results = [list(r) for r in results]

        return results
