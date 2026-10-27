class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        maxf = 0
        l = 0
        res = 0

        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)
            maxf = max(char_map[s[r]], maxf)

            while (r - l + 1) - maxf > k:
                char_map[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)
        
        return res