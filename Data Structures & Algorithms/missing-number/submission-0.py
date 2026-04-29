class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = n = len(nums)
        for i in range(n):
           res ^= i ^ nums[i]
        return res
