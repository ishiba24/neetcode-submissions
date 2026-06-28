class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #while we are less than the sum, inc r, while we are greater, dec l?
        res = float('inf')
        l = 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                curSum -= nums[l]
                res = min(res, r - l + 1)
                l += 1
            #if values not greater than curSum
        if res == float('inf'):
            res = 0
        return res