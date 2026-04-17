class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * (n + 1)

        for i in range(2, n + 1):
            memo[i] = min(cost[i - 1] + memo[i - 1], cost[i - 2] + memo[i - 2])
        
        return memo[n]

        [1, 2, 3]
        [0, 0, 1, 0]
        2