class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lett_set = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            
            while s[r] in lett_set:
                lett_set.remove(s[l])
                l += 1
            
            longest = max(longest, r - l + 1)

            lett_set.add(s[r])
        
        return longest