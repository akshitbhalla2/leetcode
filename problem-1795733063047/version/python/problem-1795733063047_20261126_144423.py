# Last updated: 11/26/2026, 2:44:23 PM
1from collections import deque 
2
3class MyStack:
4
5    def __init__(self):
6        self.queue = deque()
7
8    def push(self, x: int) -> None:
9        self.queue.append(x)
10
11    def pop(self) -> int:
12        size = len(self.queue)
13        temp = deque()
14        for _ in range(size-1):
15            q = self.queue.popleft()
16            temp.append(q)
17        x = self.queue.popleft()
18        self.queue = temp
19        return x
20
21    def top(self) -> int:
22        x = self.pop()
23        self.queue.append(x)
24        return x 
25
26    def empty(self) -> bool:
27        return False if self.queue else True
28
29
30# Your MyStack object will be instantiated and called as such:
31# obj = MyStack()
32# obj.push(x)
33# param_2 = obj.pop()
34# param_3 = obj.top()
35# param_4 = obj.empty()