class Solution:
    def partition(self, left, right, nums):
        mid = (left + right) // 2
        nums[left + 1], nums[mid] = nums[mid], nums[left + 1]
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left + 1] > nums[right]:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
        if nums[left] > nums[left + 1]:
            nums[left + 1], nums[left] = nums[left], nums[left + 1]
        pivot = nums[left + 1]
        i =left + 1
        j = right
        while True:
            while True:
                i += 1
                if  nums[i] >= pivot:
                    break
            while True:
                j -= 1
                if nums[j] <= pivot:
                    break
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left + 1], nums[j] = nums[j], nums[left + 1]
        return j
    def quicksort(self,nums, left, right):
        if right <= left + 1:
            if right == left + 1 and nums[right] < nums[left]:
                nums[left],nums[right] = nums[right], nums[left]
            return
        j = self.partition(left, right, nums)
        self.quicksort(nums, left, j - 1)
        self.quicksort(nums, j + 1, right)
    def sortArray(self, nums: List[int]) -> List[int]:
        #using quick sort, partition, quicksort
        self.quicksort(nums, 0, len(nums) - 1)
        return nums