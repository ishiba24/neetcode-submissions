class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #think of a bottom up solution, dp is the size of the board. at each position, its paths are equal to 1 + dp[i -1][j], 1 + dp[i][j - 1]
        dp = [[0] * (n) for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    print((r, c))
                    dp[r][c] = dp[r][c - 1]
                    print(dp[r][c])
                    continue
                if c == 0:
                    dp[r][c] = dp[r - 1][c]
                    continue
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[m - 1][n - 1]