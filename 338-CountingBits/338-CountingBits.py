# Last updated: 4/19/2026, 11:23:14 PM
class Solution:
    def countBits(self, n: int) -> List[int]:

        from collections import Counter

        ans = []
        for i in range(0, n+1):
            v = Counter(bin(i)[2:])["1"]
            ans.append(v)

        return ans
        