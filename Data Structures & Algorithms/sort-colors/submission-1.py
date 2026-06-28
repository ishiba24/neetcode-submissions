class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #just sorting three numbers, keep three pointers and iterate? while l and r are dont cross, continue
        l, r = 0, len(nums) - 1
        i = 0
        def swap(i, j):
            temp = nums[i] 
            nums[i] = nums[j] 
            nums[j] = temp #cant use built in sorting functions
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1 #boundary for r decreases
            else:
                i += 1
        return nums

