class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # for O(1) lookup
        memo = {}

        def dfs(i):
            # return True when reach the end
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            # Check every possible substring in word
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)
