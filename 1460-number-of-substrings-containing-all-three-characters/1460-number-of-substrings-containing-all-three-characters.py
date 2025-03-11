class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        counts = defaultdict(int)

        for r in range(len(s)):
            counts[s[r]] += 1

            while len(counts) == 3:
                res += (len(s) - r)
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    counts.pop(s[l])
                l += 1
        
        return res
