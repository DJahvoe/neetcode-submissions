class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur_str = ""
        for d in digits:
            cur_str += str(d)
        digit = int(cur_str)
        digit += 1
        str_digit = str(digit)
        return [int(s) for s in str_digit]

        