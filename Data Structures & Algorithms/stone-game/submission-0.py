class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #determine if the total is negative or positive, positive meaning alice wins
        #at each point we can take the max between the left and right sides no? actually it could be that we dont take a higher side amount if a bigger amount is behind it, so no sliding window here. 
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:
                    dp[l][r] = piles[l]
                else:
                    takeLeft = piles[l] - dp[l + 1][r]
                    takeRight = piles[r] - dp[l][r - 1]
                    dp[l][r] = max(takeLeft, takeRight)
        return dp[0][n - 1] > 0