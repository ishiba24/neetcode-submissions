class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #keep a global count of number representing target, at each step explore a path where you skip and where you add the value. if the value is > than target, end early. 
        #why 2D? keep track of take, not take at each coin? so (i, j)
        coins.sort()
        dp = {}
        def dfs(i, amt):
            if amt == 0:
                return 1
            if i >=len(coins):
                return 0
            if (i,amt) in dp:
                return dp[(i, amt)]
            res = 0
            if amt >= coins[i]:
                res += dfs(i + 1, amt)
                res += dfs(i, amt - coins[i])
            dp[(i, amt)] = res
            return res
        return dfs(0, amount)