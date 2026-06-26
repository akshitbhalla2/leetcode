class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        max_ = arr[-1]
        for i in range(l-2, -1, -1):
            v = arr[i]
            arr[i] = max_
            max_ = max(max_, v)   
        arr[-1] = -1
        return arr

        
