class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_p = max(max_p, profit)
            else:
                buy = sell
            sell += 1
        return max_p
