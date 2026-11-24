# Last updated: 11/15/2026, 5:14:10 PM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # l = len(arr)
        # max_ = arr[-1]
        # for i in range(l - 2, -1, -1):
        #     v = arr[i]
        #     arr[i] = max_
        #     max_ = max(max_, v)
        # arr[-1] = -1
        # return arr

        size = len(arr)
        max_ = -float("inf")
        prev = arr[-1]
        arr[-1] = -1
        for i in range(size - 2, -1, -1):
            curr = arr[i]
            max_ = max(max_, prev)
            arr[i] = max_
            prev = curr
        return arr