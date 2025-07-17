class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        longest = 0
        l = 0

        for r in range(len(s)):

            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            longest = max(r - l + 1, longest)
            charset.add(s[r])
        
        return longest
