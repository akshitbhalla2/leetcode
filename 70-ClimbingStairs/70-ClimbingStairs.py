# Last updated: 4/19/2026, 11:23:51 PM
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 1:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        n1 = 1
        n2 = 2
        for _ in range(2, n):
            total = n1 + n2
            n1 = n2
            n2 = total 
        
        return total