class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n)
        return self.dfs(0, n, memo)
    def dfs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] != 0:
            return memo[i]
        memo[i] = self.dfs(i + 1, n, memo) + self.dfs(i + 2, n, memo)
        return memo[i]