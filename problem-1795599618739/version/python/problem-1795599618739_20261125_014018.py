# Last updated: 11/25/2026, 1:40:18 AM
1class Solution:
2    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
3
4        size = len(sandwiches)
5
6        for i in range(size):
7            sandwich = sandwiches[i]
8            for j in range(size-i):
9                student = students.pop(0)
10                if sandwich == student:
11                    break
12                students.append(student)
13            else:
14                return size - i
15
16        return 0 
17
18                