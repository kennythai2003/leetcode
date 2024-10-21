class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0

        for p in prices[1:]:

            if p < low:
                low = p
            
            profit = max(profit, p - low)
        

        return profit