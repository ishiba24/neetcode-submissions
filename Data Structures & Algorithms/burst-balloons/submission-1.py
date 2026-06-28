class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #need to conside the value at the balloon, and the value greater than or equal. at each position you can either pop or not pop
        newNums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n + 2) for i in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = newNums[l - 1] * newNums[i] * newNums[r + 1]
                    bestLeft = dp[l][i - 1] 
                    bestRight = dp[i + 1][r]
                    pos = coins + bestLeft + bestRight
                    dp[l][r] = max(dp[l][r], pos)
        return dp[1][n]
