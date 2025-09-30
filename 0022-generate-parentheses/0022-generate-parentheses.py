class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        string = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(string))
                return
            
            if openN < n:
                string.append("(")
                backtrack(openN + 1, closeN)
                string.pop()
            
            if closeN < openN:
                string.append(")")
                backtrack(openN, closeN + 1)
                string.pop()

        backtrack(0, 0)
        return res