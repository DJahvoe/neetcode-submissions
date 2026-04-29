class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count = 0
        def dfs(i, cur_sum):
            nonlocal count

            if i == len(nums):
                if target == cur_sum:
                    count += 1
                return
            
            # add to the sum
            cur_sum += nums[i]
            dfs(i + 1, cur_sum)
            cur_sum -= nums[i]

            # substract to the sum
            cur_sum -= nums[i]
            dfs(i + 1, cur_sum)
            cur_sum += nums[i]

        dfs(0, 0)
        return count