class Solution:
    def getSum(self, a: int, b: int) -> int:
        c = 0
        res = 0
        mask = 0xFFFFFFFF
        
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ c
            c = (a_bit + b_bit + c) >= 2
            if cur_bit:
                res |= (1 << i)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res