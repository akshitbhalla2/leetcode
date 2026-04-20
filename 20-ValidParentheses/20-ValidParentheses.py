# Last updated: 4/19/2026, 11:24:07 PM
class Solution:
    def isValid(self, s: str) -> bool:

        par_map = {")": "(", "}": "{", "]": "["}
        open_set = {"(", "{", "["}

        stack = []
        for c in s:
            
            if c in open_set:
                stack.append(c)
            
            else:
                
                if not stack:
                    return False
                
                e = stack.pop()
                if e != par_map[c]:
                    return False

        if stack:
            return False

        return True
            

