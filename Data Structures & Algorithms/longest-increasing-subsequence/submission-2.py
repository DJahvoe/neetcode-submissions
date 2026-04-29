class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = [1 for num in nums]
        for i in range(len(table) - 1, -1, -1):
            for j in range(i, len(table)):
                if nums[i] < nums[j]:
                    table[i] = max(table[i], table[j] + 1)
            
        return max(table)