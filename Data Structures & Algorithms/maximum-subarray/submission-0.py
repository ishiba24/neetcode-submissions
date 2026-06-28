class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #choose the highest value in the array each pass, how can we keep track without passing over mutliple
        #dp, at each number choose to extend if number adds to sum?
        res = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            res = max(res, curSum)
        return res
