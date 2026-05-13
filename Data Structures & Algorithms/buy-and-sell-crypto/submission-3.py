class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        m = 0

        # move the sell pointer forward
        # at each index checking if its a lower price
        # than our current buy, if so change it,
        # otherwise see if its max profit
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                m = max(m, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return m








        