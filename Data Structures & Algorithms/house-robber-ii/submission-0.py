class Solution:
    def rob(self, nums: List[int]) -> int:
        #same solution to hr1, but account for circle? cant have last and first house, so run two versions and take max, exclude last and first
       return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for curVal in nums:
            newVal = max(rob1 + curVal, rob2)
            rob1 = rob2
            rob2 = newVal
        return rob2