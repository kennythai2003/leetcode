class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        for j in range(1, amount + 1):
            for coin in coins:
                if coin <= j:
                    dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
