class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxProfit = 0
        l = 0
        for r in range(len(nums)):
            profit = nums[r] - nums[l]
            maxProfit = max(profit, maxProfit)
            if nums[r] < nums[l]:
                l = r
        return maxProfit