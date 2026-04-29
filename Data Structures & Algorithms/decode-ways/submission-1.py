class Solution:
    def numDecodings(self, s: str) -> int:
        total = 0
        memo = {len(s): 1}
        # edge case
        if len(s) == 0 or s[0] == "0":
            return 0

        def dfs(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            
            # take one character at once
            t_one = dfs(i + 1)

            # take two characters at once if possible
            t_two = 0
            if (i + 1) < len(s) and int(s[i] + s[i+1]) <= 26:
                t_two = dfs(i + 2)

            memo[i] = t_one + t_two
            return memo[i]

        return dfs(0)
        