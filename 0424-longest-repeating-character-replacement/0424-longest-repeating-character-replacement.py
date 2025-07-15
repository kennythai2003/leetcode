class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = {}
        l = 0
        longest = 0
        maxf = 0

        for r in range(len(s)):
            charmap[s[r]] = 1 + charmap.get(s[r], 0)
            maxf = max(maxf, charmap[s[r]])
            if (r - l + 1) - maxf > k:
                charmap[s[l]] -= 1
                l += 1
            longest = max(r - l + 1, longest)
        
        return longest

            
