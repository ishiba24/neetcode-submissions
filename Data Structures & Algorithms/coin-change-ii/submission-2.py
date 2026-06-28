class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #keep a global count of number representing target, at each step explore a path where you skip and where you add the value. if the value is > than target, end early. 
        #why 2D? keep track of take, not take at each coin? so (i, j)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for a in range(1, amount + 1):
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
        return dp[amount]