class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two ptrs, one indexed, since sorted we know we will hit it eventually forward
        #calculate diff, use second ptr to iterate through
        l = 0
        r = len(nums) - 1
        while l < r:
            curSum = nums[l] + nums[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]