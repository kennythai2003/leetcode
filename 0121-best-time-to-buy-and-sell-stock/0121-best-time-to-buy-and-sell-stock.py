class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        maxp = 0
        l = 0
        for r in range(len(prices)):
            
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(profit, res)
            else:
                l = r
            
        return res
