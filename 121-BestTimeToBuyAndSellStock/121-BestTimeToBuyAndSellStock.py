# Last updated: 4/19/2026, 11:23:42 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        size = len(prices)

        buy = prices[0]
        profit = 0
        
        for i in range(1, size):

            sell = prices[i]
            
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit