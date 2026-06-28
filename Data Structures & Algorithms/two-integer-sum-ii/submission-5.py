class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #two ptrs, one indexed, since sorted we know we will hit it eventually forward
        #calculate diff, use second ptr to iterate through
        l = 0
        r = 1
        while l <= r:
            while r < len(nums):
                diff = target - nums[l]
                if nums[r] == diff:
                    return [l + 1, r + 1]
                r += 1
            l += 1
            r = l

            
            