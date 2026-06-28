class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #must edit list and return k
        #use set? two ptrs tho, compare adj elements
        #rebuild array, l marks next unique spot, r scans through
        if not nums:
            return 0
        l = 1
        k = 1
        for r in range(1,len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
                k += 1
        return k
            

