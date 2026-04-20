# Last updated: 4/19/2026, 11:23:53 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        size = len(digits)

        new_d = 10

        for i in range(size-1, -1, -1):
            rem = new_d - 9
            new_d = digits[i] + rem

            if new_d <= 9:
                digits[i] = new_d
                return digits
            
            digits[i] = new_d - 10

        return [rem] + digits


            

                
            

        