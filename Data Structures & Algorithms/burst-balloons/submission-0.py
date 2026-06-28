class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #need to conside the value at the balloon, and the value greater than or equal. at each position you can either pop or not pop
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r +1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                bestLeft = dfs(l, i -1)
                bestRight = dfs(i + 1, r)
                pos = coins + bestLeft + bestRight
                dp[(l,r)] = max(dp[(l,r)], pos)
            return dp[(l, r)]
        return dfs(1, len(nums) - 2)