class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0 
        maxf = 0
        l = 0

        charmap = {}
        for r in range(len(s)):
            
            charmap[s[r]] = 1 + charmap.get(s[r] , 0)

            maxf = max(maxf, charmap[s[r]])
            while (r - l + 1) - maxf > k:
                charmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            