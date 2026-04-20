# Last updated: 4/19/2026, 11:23:19 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True
        
        return False

        # s = s.split("")
        # s.sort()
        
        # t = t.split("")
        # t.sort()

        # print("#", s)
        # print("#", t)

        # s = "".join(s)
        # t = "".join(t)

        # print("@", s)
        # print("@", t)

        # if s == t:
        #     return True
        
        # return False