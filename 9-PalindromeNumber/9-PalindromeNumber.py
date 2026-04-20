# Last updated: 4/19/2026, 11:24:11 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        digits = []
        size = 0
        while x >= 10:
            digit = x % 10
            x = x // 10
            digits.append(digit) 
            size += 1

        digits.append(x)
        size += 1
        
        for i in range(size//2):
            if digits[i] == digits[size-1-i]:
                continue
            else:
                return False

        return True

