# Last updated: 11/15/2026, 5:21:40 PM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size = len(arr)
        max_ = arr[-1]
        arr[-1] = -1
        for i in range(size-2, -1, -1):
            curr = arr[i]
            arr[i] = max_
            max_ = max(max_, curr)
        return arr

        