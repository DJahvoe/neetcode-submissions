class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if len(prices) == 1:
            return 0
        else:
            buy = 0
            maxProfit = 0
            for sell in range(1, len(prices)):
                profit = prices[sell] - prices[buy]
                if(maxProfit < profit):
                    maxProfit = profit
                if prices[sell] < prices[buy]:
                    buy = sell
            return maxProfit
        
                