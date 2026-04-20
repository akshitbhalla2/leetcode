# Last updated: 4/20/2026, 1:17:46 AM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # size = len(arr)
        # m = float('-inf')
        # maxes = []
        # for i in range(size-1, 0, -1):
        #     m = max(m, arr[i])
        #     maxes.insert(0, m)
        # maxes.append(-1)
        # return maxes

        size = len(arr)
        m = float('-inf')
        last = arr[-1]
        arr[-1] = -1
        for i in range(size-2, -1, -1): 
            m = max(m, last)
            last = arr[i]
            arr[i] = m
        return arr