class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        #just sort and go inwards? if it doesnt work, move the corresponding pointer?
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] > limit:
                res += 1
                r -= 1
            elif nums[l] + nums[r] <= limit:
                res += 1
                l += 1
                r -= 1
        return res
        #how to handle odd boats/people vals?
