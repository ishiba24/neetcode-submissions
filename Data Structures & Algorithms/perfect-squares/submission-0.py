class Solution:
    import math
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, math.isqrt(n) + 1):
            squares.append(i * i)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for num in range(1, n + 1):
            for sq in squares:
                dp[num] = min(dp[num], 1 + dp[num - sq])
        return dp[n]