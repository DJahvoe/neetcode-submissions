class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = 0

        p = len(cost) - 1
        q = p - 1
        while p >= 0 and q >= 0:
            print(p, q)
            print(total_cost)
            if cost[q] <= cost[p]:
                total_cost += cost[q]
                p -= 2
            else:
                total_cost += cost[p]
                p -= 1
            q = p - 1
        return total_cost