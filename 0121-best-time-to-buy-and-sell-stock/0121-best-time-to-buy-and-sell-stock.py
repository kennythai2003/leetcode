class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_prof = 0
        l = prices[0]
        for p in prices:
            if l < p:
                max_prof = max(p - l, max_prof)
            else:
                l = p
        
        return max_prof