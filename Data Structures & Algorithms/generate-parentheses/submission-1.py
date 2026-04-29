class Solution:
    def sumAllDigit(self, binaryStr):
        digitSum = 0
        for i in binaryStr:
            digitSum += int(i)
        return digitSum

    def isParenthesisValid(self, parenthesisStr):
        parenthesisStack = []
        for p in parenthesisStr:
            if p == '(':
                parenthesisStack.append(p)
            else:
                if len(parenthesisStack) == 0:
                    return False
                parenthesisStack.pop()
        if len(parenthesisStack) > 0:
            return False
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        candidateCounts = 2 ** (2*n)
        # Generate all the possibilities
        generatedItems = [bin(x).replace("0b", "") for x in range(candidateCounts // 2, candidateCounts)]
        # Exclude all binary with sum of digit that Odd-Numbered
        generatedItems = list(filter(lambda x: self.sumAllDigit(x) % 2 == (n % 2), generatedItems))
        # Convert binary to parenthesis
        generatedItems = [item.replace("1", "(").replace("0", ")") for item in generatedItems]
        # Remove invalid combinations
        generatedItems = list(filter(lambda item: self.isParenthesisValid(item), generatedItems))
        return generatedItems
        