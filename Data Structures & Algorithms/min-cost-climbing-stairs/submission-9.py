class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cache = [-1] * len(cost)
        # def dfs(i):
        #     # base condition
        #     if i >= len(cost):
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[i]

        # # You can either start from 0 or 1
        # return min(dfs(0), dfs(1))

        #space optimisation
        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
        