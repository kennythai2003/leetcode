class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        maxp = 0

        l = 0

        for r in range(len(prices)):

            if prices[l] < prices[r]:
                maxp = max(prices[r] - prices[l], maxp)
            else:
                l = r
        
        return maxp