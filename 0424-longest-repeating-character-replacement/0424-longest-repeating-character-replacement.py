class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charmap = {}
        maxf = 0
        res = 0
        l = 0

        for r in range(len(s)):
            charmap[s[r]] = 1 + charmap.get(s[r], 0)
            maxf = max(charmap[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                charmap[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        
        return res