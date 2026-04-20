# Last updated: 4/19/2026, 11:23:38 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        stringLen = len(s)
        dp = [False] * (stringLen + 1)
        dp[-1] = True

        for i in range(stringLen - 1, -1 , -1):
            for w in wordDict:
                wordLen = len(w)
                if s[i : i + wordLen] == w:
                    dp[i] = dp[i + wordLen]

                if dp[i] == True:
                    break
        
        return dp[i]