class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1 for num in nums]
        max_res = 0
        for i in range(len(table) - 1, -1, -1):
            cur_num = nums[i]
            cur_max = table[i]
            for j in range(i, len(table)):
                if cur_num < nums[j]:
                    cur_max = max(cur_max, table[j] + 1)
            table[i] = cur_max
            max_res = max(max_res, cur_max)
            
        return max_res