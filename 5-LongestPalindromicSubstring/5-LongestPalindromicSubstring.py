# Last updated: 4/19/2026, 11:24:12 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return 0

        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        pal = s[0]
        pal_len = 1

        for i in range(0, n):
            dp[i][i] = 1

        for i in range(1, n):
            if s[i-1] == s[i]:
                dp[i-1][i] = 2
                pal = s[i-1:i+1]
                pal_len = 2
            else:
                dp[i-1][i] = 0

        for i in range(2, n):
            for j in range(i, n):
                
                a = j - i
                b = j

                if s[a] != s[b]:
                    dp[a][b] = 0
                
                else: 
                    if dp[a+1][b-1] == 0:
                        dp[a][b] = 0
                    else:
                        dp[a][b] = dp[a+1][b-1] + 2
                    
                        if dp[a][b] > pal_len: 
                            pal = s[a:b+1]
                            pal_len = dp[a][b] 

        return pal

        

