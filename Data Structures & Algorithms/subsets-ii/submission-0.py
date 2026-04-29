class Solution:
    def helper(self, index, nums, cursub, allsub):
        if index >= len(nums):
            allsub.append(cursub.copy())
            return
        
        cursub.append(nums[index])
        self.helper(index + 1, nums, cursub, allsub)

        cursub.pop()
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
           index += 1
        self.helper(index + 1, nums, cursub, allsub)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cursub, allsub = [], []
        self.helper(0, nums, cursub, allsub)
        return allsub
        