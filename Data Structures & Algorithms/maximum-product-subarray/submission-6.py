class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #build out the max value so far in the dp array at each step, then 
        #set dp[i] = max(dp[i - 1], dp[i - 1] + nums[i]), but we need a special case for two negatives no?
        n = len(nums)
        if n == 1:
            return nums[0]
        minDp = [0] * n
        maxDp = [0] * n
        minDp[0], maxDp[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(n):
            maxDp[i] = max(nums[i] * maxDp[i-1], nums[i] * minDp[i-1], nums[i])
            minDp[i] = min(nums[i] * maxDp[i - 1], nums[i] *minDp[i-1], nums[i])
            res = max(res, maxDp[i])
        return res