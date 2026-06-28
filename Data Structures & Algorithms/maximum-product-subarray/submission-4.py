class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #must be consecutive elements, create a memo array holding the max product at each index in the nums array
        #take max(nums[i], dp[i + 1])?
        #kadanes algorithm, keep track of curMax and curMin of each index, in order to handle neg and pos vals. if we have 0, rst max and min to 1(ignore them)
        res = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            tmp = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, tmp * num, curMin * num)
            res = max(curMax, res)
        return res