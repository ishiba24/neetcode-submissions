class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #in place sort, sorting algorithm? insertion sort type of problem? counting sort, count num of appearances and then place
        l, r = 0, len(nums) - 1
        i = 0 

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
            else:
                i += 1

            
