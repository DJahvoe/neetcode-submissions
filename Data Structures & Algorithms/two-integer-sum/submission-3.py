class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if nums[i] in pair:
                return [pair[nums[i]], i]
            pair[other] = i
