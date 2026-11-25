# Last updated: 11/25/2026, 1:40:18 AM
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        size = len(sandwiches)

        for i in range(size):
            sandwich = sandwiches[i]
            for _ in range(size - i):
                student = students.pop(0)
                if sandwich == student:
                    break
                students.append(student)
            else:
                return size - i

        return 0