class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            if n > 0:
                res *= x
            else:
                res *= (1 / x)
            print(res)
        return res