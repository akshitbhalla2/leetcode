# Last updated: 11/26/2026, 2:44:23 PM
from collections import deque

# Stack: read, write, and remove all happen at the top.
# Queue: write at the rear; read and remove at the front.

# # push: O(1), pop: O(n), top: O(n)
# class MyStack:

#     def __init__(self):
#         self.queue = deque()

#     def push(self, x: int) -> None:
#         self.queue.append(x)

#     def pop(self) -> int:
#         for _ in range(len(self.queue)-1):
#             self.queue.append(self.queue.popleft())
#         return self.queue.popleft()

#     def top(self) -> int:
#         x = self.pop()
#         self.push(x)
#         return x

#     def empty(self) -> bool:
#         return not self.queue

# push: O(n), pop: O(1), top: O(1)
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()