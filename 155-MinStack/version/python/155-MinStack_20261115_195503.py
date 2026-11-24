# Last updated: 11/15/2026, 7:55:03 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = float("inf")

    def push(self, value: int) -> None:
        self.min_ = min(self.min_, value)
        self.stack.append((value, self.min_))

    def pop(self) -> None:
        self.stack.pop()
        self.min_ = self.stack[-1][1] if self.stack else float("inf")

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
