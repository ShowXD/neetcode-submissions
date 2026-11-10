class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            if prices[i] > cost:
                max_profit = max(prices[i] - cost, max_profit)
        return max_profit
        