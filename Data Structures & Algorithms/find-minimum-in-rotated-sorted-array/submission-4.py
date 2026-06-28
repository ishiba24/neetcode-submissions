class Solution:
    def findMin(self, nums: List[int]) -> int:
        #use the middle element, but find the pivot points. if mid is greater than l, working in sorted area
        #if mid is less than l, pivot is in between so r = m - 1
        l, r = 0, len(nums) - 1
        curMin = float('inf')
        while l <= r:
            if nums[l] <= nums[r]:
                curMin = min(curMin, nums[l])
                break
            m = (l + r) // 2
            curMin = min(curMin, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return curMin