class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp, dp1, dp2 = 0, 0, 0
        for i in range(2, n + 1):
            dp = min(dp1 + cost[i-1] , dp2 + cost[i-2])
            dp1, dp2 = dp, dp1
        return dp1
