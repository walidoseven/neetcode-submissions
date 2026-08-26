class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        a=0
        v=1
        profit = 0

        while v<len(prices):
            if prices[a] < prices[v]:
                current_profit = prices[v] - prices[a]
                profit = max(profit, current_profit)
            else:
                a=v
            v += 1
        return profit


