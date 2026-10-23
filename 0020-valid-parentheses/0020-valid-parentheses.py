class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}":"{", "]":"[", ")":"("}
        stack = []

        for c in s:

            if stack and stack[c] in pairs:
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append[c]


        return not stack