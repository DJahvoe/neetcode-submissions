class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        l = 0
        cur_sum = 0
        total_sum = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            cur_sum += diff
            total_sum += diff

            if cur_sum < 0:
                l = i + 1
                cur_sum = 0
        
        if l == len(gas) or total_sum < 0:
            return -1
        return l

