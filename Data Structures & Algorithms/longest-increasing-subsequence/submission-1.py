class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #create a dp and rmb the lis at a specific index onwards
        #use a dp array
        dp = [-1] * (len(nums))
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            dp[i] = res
            return res
        return max(dfs(i) for i in range(len(nums)))