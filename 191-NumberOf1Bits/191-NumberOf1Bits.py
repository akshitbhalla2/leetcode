# Last updated: 4/19/2026, 11:23:28 PM
class Solution:
    def hammingWeight(self, n: int) -> int:

        from collections import Counter

        return Counter(bin(n)[2:])["1"]
        