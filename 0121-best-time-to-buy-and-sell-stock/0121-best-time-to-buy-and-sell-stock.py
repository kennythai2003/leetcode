class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                max_profit = max(max_profit, profit)
            else:
                l = r
        
        return max_profit