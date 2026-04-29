from functools import reduce
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[len(piles) - 1]
        minEatingRate = -1
        print(piles)
        while left != right:
            middle = (left + right) // 2
            k = middle
            pileSum = reduce((lambda total, x: total + math.ceil(x / k)), piles, 0)
            print()
            print("----")
            print(left, right, middle)
            print(k)
            print(pileSum)
            
            if pileSum > h:
                left = middle + 1
            else:
                right = middle
        return left
            