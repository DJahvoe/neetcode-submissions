class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tempMax = max(n, n * curMax, n * curMin)
            tempMin = min(n, n * curMax, n * curMin)

            curMax, curMin = tempMax, tempMin
            res = max(res, curMax)

        return res
