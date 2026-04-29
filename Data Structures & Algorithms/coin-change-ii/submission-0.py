class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[a] = number of combinations to make amount a
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            # Iterate amounts forward so each coin contributes combinations (not permutations).
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]