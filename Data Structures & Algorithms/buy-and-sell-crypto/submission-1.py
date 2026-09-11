class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       maxProfit = 0
       minBuy = prices[0]

       for sell in prices:
          profit = sell - minBuy
          if profit > maxProfit:
            maxProfit = profit
        
          if sell < minBuy:
            minBuy = sell

       return maxProfit
