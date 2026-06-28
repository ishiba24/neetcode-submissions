class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            while nums[l] != 0 and l < len(nums) - 1:
                l += 1
            if nums[r] == 0 or r < l:
                continue
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
            
            
