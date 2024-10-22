class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charfreq = {}
        l = 0
        longest  = 0

        for r in range(len(s)):
            
            charfreq[s[r]] = 1 + charfreq.get(s[r], 0)
            if ((r - l + 1) - max(charfreq.values())) > k:
                charfreq[s[l]] -= 1
                l += 1
            longest = max(r - l + 1, longest)
        
        return longest
        