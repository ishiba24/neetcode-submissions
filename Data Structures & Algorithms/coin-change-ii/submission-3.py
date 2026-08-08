class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        #at each step you can either take the coin, or skip it. taking it is equal to dp[i][a-coin[i]], skipping it is just dp[i + 1][a]
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        return dp[i][amount]