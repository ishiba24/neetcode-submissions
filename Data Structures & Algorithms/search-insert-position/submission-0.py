class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search?
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l

            
