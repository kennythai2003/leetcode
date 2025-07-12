class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # One way to stand at the ground (0th step)
        dp[1] = 1  # One way to reach the 1st step

        for stair in range(2, n + 1):
            for step in range(1, 3):  # step = 1 or 2
                dp[stair] += dp[stair - step]

        return dp[n]
