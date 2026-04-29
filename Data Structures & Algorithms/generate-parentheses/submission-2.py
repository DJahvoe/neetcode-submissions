class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generated = []

        def isValid(s: str):
            left = 0
            for current in s:
                left += (-1, 1)[current == '(']
                if left < 0:
                    return False
            
            if left > 0:
                return False
            return True

        def dfs(currentStr: str):
            if n * 2 == len(currentStr):
                if isValid(currentStr):
                    generated.append(currentStr)
                return
            dfs(currentStr + '(')
            dfs(currentStr + ')')
        
        dfs("")
        return generated

        