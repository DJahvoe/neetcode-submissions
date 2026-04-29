class Solution:
    def nextNum(self, n):
        num = 0
        while n > 0:
            num += (n % 10) ** 2
            n //= 10
        return num

    def isHappy(self, n: int) -> bool:
        num_collection = defaultdict(int)
        while n != 1:
            if n in num_collection:
                return False
            num_collection[n] += 1
            n = self.nextNum(n)
        return True
            
