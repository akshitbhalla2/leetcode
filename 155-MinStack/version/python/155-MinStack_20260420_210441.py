# Last updated: 4/20/2026, 9:04:41 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.mins = []       
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9        if not self.mins:
10            self.mins.append(val)
11        else:
12            self.mins.append(min(self.mins[-1], val))
13
14    def pop(self) -> None:
15        self.stack.pop()
16        self.mins.pop()
17
18    def top(self) -> int:
19        return self.stack[-1]
20
21    def getMin(self) -> int:
22        return self.mins[-1]
23
24
25# Your MinStack object will be instantiated and called as such:
26# obj = MinStack()
27# obj.push(val)
28# obj.pop()
29# param_3 = obj.top()
30# param_4 = obj.getMin()