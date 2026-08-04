class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #create a dp and rmb the lis at a specific index onwards
        #use a dp array
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)