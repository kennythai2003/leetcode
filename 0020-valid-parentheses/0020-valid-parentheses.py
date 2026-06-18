class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {"]":"[", ")" : "(", "}" : "{"}
        stack = []
        for c in s:

            if c in brackets_map:
                if stack and brackets_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack