class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0

        step = 0
        while l < len(nums) - 1:
            print(l, nums[l])
            cur_num = nums[l]
            max_r = -1
            max_val = float("-inf")
            for r in range(l + 1, l + 1 + cur_num):
                if r == len(nums) - 1:
                    max_r = r
                    break
                if nums[r] >= max_val:
                    max_val = nums[r]
                    max_r = r
            l = max_r
            
            step += 1
        return step