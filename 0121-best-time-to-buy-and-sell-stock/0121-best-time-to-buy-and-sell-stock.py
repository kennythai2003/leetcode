class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        l = 0

        for p in range(len(prices)):

            if prices[l] < prices[p]:
                res = max(prices[p] - prices[l], res)
            else:
                l = p
        
        return res