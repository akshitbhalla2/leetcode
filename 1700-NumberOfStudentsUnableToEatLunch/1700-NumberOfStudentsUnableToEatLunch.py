class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        # size = len(sandwiches)

        # for i in range(size):
        #     sandwich = sandwiches[i]
        #     for j in range(size-i):
        #         student = students.pop(0)
        #         if sandwich == student:
        #             break
        #         students.append(student)
        #     else:
        #         return size - i

        # return 0 

        size = len(sandwiches)

        count = 0
        while True:

            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                count = 0
            
            else:
                students.append(students.pop(0))
                count += 1
            
            if count == len(students):
                break

        return count