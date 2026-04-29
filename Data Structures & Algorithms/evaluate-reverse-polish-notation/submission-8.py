class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                second, first = stack.pop(), stack.pop()
                if t == "/":
                    result = int(first / second)  # correct truncation toward 0
                else:
                    result = eval(f'{first} {t} {second}')
                print(t)
                stack.append(int(result))
            else:
                stack.append(int(t))
            print(stack)
        return stack.pop()