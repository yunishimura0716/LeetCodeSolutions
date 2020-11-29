class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost[0], cost[1])
        min_cost_arr = [0] * len(cost)
        min_cost_arr[0] = cost[0]
        min_cost_arr[1] = cost[1]
        for i in range(2, len(cost) - 1):
            min_cost_arr[i] = cost[i] + min(min_cost_arr[i-1], min_cost_arr[i-2])
        min_cost_arr[-1] = cost[-1] + min_cost_arr[-3]
        return min(min_cost_arr[-1],  min_cost_arr[-2])
