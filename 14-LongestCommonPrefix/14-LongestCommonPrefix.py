# Last updated: 4/19/2026, 11:24:08 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        short = ""
        short_len = 201

        for word in strs:
            word_len = len(word)
            if word_len < short_len:
                short_len = word_len
                short = word

        prefix = ""
        for i, l in enumerate(short):
            for word in strs:
                if word[i] == l:
                    continue
                else:
                    return prefix
            prefix += l

        return prefix


