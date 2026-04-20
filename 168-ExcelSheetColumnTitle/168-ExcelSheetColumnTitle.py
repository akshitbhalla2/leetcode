# Last updated: 4/19/2026, 11:23:33 PM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        import math

        name = ""
        while columnNumber > 26:
        
            rem = columnNumber % 26
            rem = 26 if rem == 0 else rem

            name  = chr(rem + 64) + name

            columnNumber = math.ceil((columnNumber - rem) / 26)

        rem = columnNumber % 26 
        rem = 26 if rem == 0 else rem

        name  = chr(rem + 64) + name

        return name

