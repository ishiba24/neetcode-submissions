class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #keep a global count of number representing target, at each step explore a path where you skip and where you add the value. if the value is > than target, end early. 
        #why 2D? keep track of take, not take at each coin? so (i, j)
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(n -1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] += dp[i + 1][a]
                    dp[i][a] += dp[i][a-coins[i]]
        return dp[0][amount]