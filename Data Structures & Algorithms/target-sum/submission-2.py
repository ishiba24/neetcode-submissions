class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #very similar to coin change, but now you either sub or add instead of skipping?
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+ 1)]
        dp[0][0] = 1
        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]