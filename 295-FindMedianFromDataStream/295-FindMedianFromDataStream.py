# Last updated: 4/19/2026, 11:23:16 PM
class MedianFinder:

    def __init__(self):
        self.numbers = []

    def getIndex(self, target):

        size = len(self.numbers)
        left = 0
        right = size - 1
        
        while left <= right:

            mid = left + (right - left) // 2

            if self.numbers[mid] == target:
                return mid

            if left == right:
                if target > self.numbers[left]:
                    return left + 1
                else:
                    return left
            
            if target > self.numbers[mid]:
                left = mid + 1
            else:
                right = mid

        return left

    def addNum(self, num: int) -> None:
        index = self.getIndex(num)
        self.numbers.insert(index, num)
        # print("#", self.numbers)

    def findMedian(self) -> float:
        size = len(self.numbers)
        if size % 2 != 0:
            return self.numbers[size//2]
        else:
            return (self.numbers[size//2] + self.numbers[size//2 - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()