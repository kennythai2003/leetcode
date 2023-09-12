class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {"]":"[", 
                ")":"(",
                "}":"{"}
        
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack