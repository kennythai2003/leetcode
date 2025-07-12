class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Initialize first row and first column to 1
        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1

        # Fill in the rest
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
