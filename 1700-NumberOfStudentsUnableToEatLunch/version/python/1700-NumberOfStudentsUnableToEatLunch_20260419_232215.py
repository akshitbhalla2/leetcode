# Last updated: 4/19/2026, 11:22:15 PM
# from collections import deque

# class deque:
#     def __init__(self, array):
#         self.array = array
#         self.head = array[0]
#         self.tail = array[-1]

#     def __

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        size = len(students)

        # students = deque(students)
        # sandwiches = deque(sandwiches)

        count = 0
        while students:

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
            
            else:
                students.append(students.pop(0))
                count += 1

            if count == len(students):
                break

        return count