# Last updated: 4/19/2026, 11:24:03 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        hlen = len(haystack)
        nlen = len(needle)

        i = 0
        
        while i < hlen:
            if haystack[i] == needle[0]:
                j = 1
                k = i+1
                while (j < nlen) and (k < hlen):
                    if haystack[k] != needle[j]:
                        break

                    j += 1
                    k += 1

                if j == nlen:
                    return k-nlen

            i += 1

        return -1