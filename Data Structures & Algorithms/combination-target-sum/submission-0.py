class Solution:
    def helper(self, nums, curr, result, target, curr_total):
        if curr_total == target:
            result.append(curr.copy())
            return
        if curr_total > target:
            return

        for i in nums:
            if len(curr) > 0 and curr[-1] > i:
                continue
            curr_total += i
            curr.append(i)
            self.helper(nums, curr, result, target, curr_total)
            curr_total -= i
            curr.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.helper(nums, [], result, target, 0)
        return result
        