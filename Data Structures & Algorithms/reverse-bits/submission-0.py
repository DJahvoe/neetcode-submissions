class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 1
        while n > 0:
            bit = n & 1
            if bit == 1:
                res |= (1 << (32 - i))
            n >>= 1
            i += 1
            print(bin(res)[2:])
        
        return res
        