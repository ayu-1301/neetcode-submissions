class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            profit = sell - minBuy
            if profit > maxP:
                maxP = profit
            
            if sell < minBuy:
                minBuy = sell
            

        return maxP
    