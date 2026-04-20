# Last updated: 4/19/2026, 11:23:15 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)

        coins.sort()

        for amt in range(1, amount + 1):

            minn = float("inf")
            
            for coin in coins:
                
                diff = amt - coin
                
                if diff < 0:
                    break

                minn = min(minn, dp[diff] + 1)
            
            dp[amt] = minn

        if dp[-1] < float("inf"):
            return dp[-1] 
        
        return -1



        