class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}

        l = 0
        longest = 0
        maxfreq = 0
        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)
            maxfreq = max(maxfreq, char_map[s[r]])

            while (r - l + 1) - maxfreq > k:
                char_map[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
            

            