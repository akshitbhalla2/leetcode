# Last updated: 11/15/2026, 7:55:03 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.min_ = float("inf")        
6
7    def push(self, value: int) -> None:
8        self.min_ = min(self.min_, value)
9        self.stack.append((value, self.min_))
10
11    def pop(self) -> None:
12        self.stack.pop()
13        self.min_ = self.stack[-1][1] if self.stack else float("inf") 
14
15    def top(self) -> int:
16        return self.stack[-1][0]
17
18    def getMin(self) -> int:
19        return self.stack[-1][1]
20        
21
22
23# Your MinStack object will be instantiated and called as such:
24# obj = MinStack()
25# obj.push(value)
26# obj.pop()
27# param_3 = obj.top()
28# param_4 = obj.getMin()