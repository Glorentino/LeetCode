# 121. Best Time to Buy and Sell Stock
# Easy

class Solution:
    def maxProfit(self, prices):
        
        cheap = prices[0]
        maxP = 0
        
        for i in range(1, len(prices)):
            cheap = min(cheap, prices[i])
            maxP = max(maxP, prices[i]-cheap)
        
        return maxP