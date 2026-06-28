class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #very similar to coin change, but now you either sub or add instead of skipping?
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            nextDp = defaultdict(int)
            for total, count in dp.items():
                nextDp[total + num] += count
                nextDp[total - num] += count
            dp = nextDp
        return dp[target]