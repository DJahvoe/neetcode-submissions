class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}

        def dfs(i, diff):
            key = (i, diff)

            if key in memo:
                return memo[key]

            if i == len(stones):
                return abs(diff)

            # add current stone to group1
            pick1 = dfs(i + 1, diff + stones[i])

            # add current stone to group2
            pick2 = dfs(i + 1, diff - stones[i])

            memo[key] = min(pick1, pick2)
            return memo[key]

        return dfs(0, 0)