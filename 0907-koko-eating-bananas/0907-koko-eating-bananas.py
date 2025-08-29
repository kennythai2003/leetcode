class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            time = 0
            k = (l + r) // 2
            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
