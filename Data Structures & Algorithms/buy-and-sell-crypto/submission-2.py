class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        m = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                m = max(m, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return m








        