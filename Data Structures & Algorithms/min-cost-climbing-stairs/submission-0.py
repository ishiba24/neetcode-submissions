class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #must reach the top step, create a memo of how expensive it is from each step by doing min(i + 1)(i + 2)
        #call it from 0 and 1, ends when we reach i == len(cost), if i > than last step return, == return cost
        n = len(cost)
        memo = [-1] * n
        def dfs(i):
            if i >= n:
                return 0 #step is reached or we passed it
            if memo[i] != -1:
                return memo[i] #already calculated
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]
        return min(dfs(0), dfs(1))
            