class Solution:
    def helper(self, index, nums, current_subsets, all_subsets):
        if index >= len(nums):
            all_subsets.append(current_subsets.copy())
            return
        
        # include element to subset
        current_subsets.append(nums[index])
        self.helper(index + 1, nums, current_subsets, all_subsets)
        current_subsets.pop()

        self.helper(index + 1, nums, current_subsets, all_subsets)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cursub, allsub = [], []
        self.helper(0, nums, cursub, allsub)
        return allsub
        