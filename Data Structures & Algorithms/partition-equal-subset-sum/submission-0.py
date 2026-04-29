class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sum1 = sum2 = 0
        def dfs(i):
            nonlocal sum1
            nonlocal sum2
            if i == len(nums):
                return sum1 == sum2
            
            # add to the first sum
            sum1 += nums[i]
            is_first_possible = dfs(i + 1)
            sum1 -= nums[i]

            # add to the second sum
            sum2 += nums[i]
            is_second_possible = dfs(i + 1)
            sum2 -= nums[i]

            return is_first_possible or is_second_possible
        
        return dfs(0)