from functools import reduce
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left != right:
            middle = (left + right) // 2
            k = middle
            pileSum = reduce((lambda total, x: total + math.ceil(x / k)), piles, 0)
            
            if pileSum > h:
                left = middle + 1
            else:
                right = middle
        return left
            