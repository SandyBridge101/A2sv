class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        memo = {}
        cost.append(0)
        def func(n):
            if n in memo:
                return memo[n]
            if n<2:
                return cost[n]

            result = min(cost[n]+func(n-1),cost[n]+func(n-2))
            memo[n] = result
            return result

        return func(n)
