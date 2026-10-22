class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxf = 0
        s_map = {}

        for r in range(len(s)):
            c = s[r]
            s_map[c] = 1 + s_map.get(c, 0)

            maxf = max(maxf, s_map[c])

            while (r - l + 1) - maxf > k:
                s_map[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res
