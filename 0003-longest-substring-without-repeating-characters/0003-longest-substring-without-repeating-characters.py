class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #charset to avoid duplicates
        charset = set()
        # when we see a dup, we remove from left, shift left
        l = 0
        
        maxl = 0
        for r in range(len(s)):

            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[r])
            maxl = max(r - l + 1, maxl)

        return maxl