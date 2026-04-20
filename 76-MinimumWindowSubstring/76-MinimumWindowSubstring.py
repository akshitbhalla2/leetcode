# Last updated: 4/19/2026, 11:23:48 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        size = len(s)

        tFreq, windowFreq = {}, {}
        for c in t:
            tFreq[c] = 1 + tFreq.get(c, 0)

        have, need = 0, len(tFreq)
        minLen = float("inf")
        pos = (-1, -1)
        l = 0
        for r in range(size):
            rChar = s[r]
            windowFreq[rChar] = 1 + windowFreq.get(rChar, 0)
            if (rChar in tFreq) and (windowFreq[rChar] == tFreq[rChar]):
                have += 1

            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    pos = (l, r)

                lChar = s[l]
                windowFreq[lChar] -= 1
                if (lChar in tFreq) and (windowFreq[lChar] < tFreq[lChar]):
                    have -= 1
                l += 1

        if minLen != float("inf"):
            l, r = pos
            return s[l:r+1]

        return ""




