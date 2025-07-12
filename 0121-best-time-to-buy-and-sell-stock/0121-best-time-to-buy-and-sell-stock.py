class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        l = 0 

        for r in range(len(prices)):

            if prices[l] < prices[r]:
                maxp = max(maxp, prices[r] - prices[l])
            else:
                l = r
        
        return maxp