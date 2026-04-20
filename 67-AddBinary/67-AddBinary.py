# Last updated: 4/19/2026, 11:23:52 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        total = int(a, 2) + int(b, 2)

        return bin(total)[2:]