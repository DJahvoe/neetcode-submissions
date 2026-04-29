class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]


            min_coin = float("inf")
            for coin in coins:
                if remaining - coin >= 0:
                    min_coin = min(min_coin, 1 + dfs(remaining - coin))

            memo[remaining] = min_coin
            return min_coin

        min_coin = dfs(amount)
        if min_coin >= float("inf"):
            return -1
        return min_coin



