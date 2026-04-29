class Solution:
    def isValid(self, s: str) -> bool:
        bracks = []

        for c in s:
            if c == "{" or c == "[" or c == "(":
                bracks.append(c)
            else:
                if len(bracks) == 0:
                    return False

                top = bracks.pop()
                if (c == "}" and top == "{")\
                    or (c == "]" and top == "[")\
                    or (c == ")" and top == "("):
                    continue
                else:
                    return False
        return len(bracks) == 0