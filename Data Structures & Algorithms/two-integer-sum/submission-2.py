class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_track = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in sum_track:
                return [sum_track[nums[i]], i]
            sum_track[diff] = i