class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffixSum = [0] * n
        suffixSum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffixSum[i] = piles[i] + suffixSum[i + 1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                for X in range(1, 2 * M + 1):
                    if i + X > n:
                        break
                    dp[i][M] = max(dp[i][M], suffixSum[i] - dp[i + X][max(M, X)])
        return dp[0][1]