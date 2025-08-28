class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_cnt = {}
        l = 0
        maxf = 0 
        res = 0

        for r in range(len(s)):

            char_cnt[s[r]] = 1 + char_cnt.get(s[r], 0)
            
            maxf = max(char_cnt[s[r]], maxf)

            while (r - l + 1) - maxf > k:
                char_cnt[s[l]] -= 1
                l += 1
            
            res = max(maxf, r - l + 1)
        
        return res
