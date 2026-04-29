class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                print(stack)
                stackTemperature, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((temperature, index))
            print(res)
        return res