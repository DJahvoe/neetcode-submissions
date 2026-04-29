class Solution:
    def helper(self, index, nums, curr, result, currTotal, target):
        if currTotal == target:
            result.append(curr.copy())
            return
        if currTotal > target:
            return
        if index >= len(nums):
            return

        currTotal += nums[index]
        curr.append(nums[index])
        self.helper(index + 1, nums, curr, result, currTotal, target)
        currTotal -= nums[index] 
        curr.pop()
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.helper(index + 1, nums, curr, result, currTotal, target)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.helper(0, candidates, [], result, 0, target)
        return result
        