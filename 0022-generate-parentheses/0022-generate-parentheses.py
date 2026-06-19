class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack (openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
            if closeN < n:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res