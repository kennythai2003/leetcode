class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in pairs:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack