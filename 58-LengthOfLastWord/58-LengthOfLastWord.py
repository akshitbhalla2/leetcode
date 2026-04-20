# Last updated: 4/19/2026, 11:23:54 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.strip().split(" ")[-1])

        size = len(s)
        
        for i in range(size-1, -1, -1):
            if s[i] == " ":
                continue
            break
        else:
            return 0
        
        k = 0
        for j in range(i, -1, -1):
            if s[j] != " ":
                k += 1
                continue
            break

        return k 