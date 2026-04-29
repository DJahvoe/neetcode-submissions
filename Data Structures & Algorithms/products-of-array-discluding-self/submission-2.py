from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        result = [0] * n

        # prefix[i] = product of all nums[0] to nums[i]
        temp = 1
        for i in range(n):
            temp *= nums[i]
            prefix[i] = temp
        
        # postfix[i] = product of all nums[i] to nums[n-1]
        temp = 1
        for i in range(n - 1, -1, -1):
            temp *= nums[i]
            postfix[i] = temp

        # build the result
        for i in range(n):
            left = 1 if i == 0 else prefix[i - 1]
            right = 1 if i == n - 1 else postfix[i + 1]
            result[i] = left * right

        print("Prefix:", prefix)
        print("Postfix:", postfix)
        print("Result:", result)

        return result
