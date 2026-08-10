class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #three cases, one where all negs which is just the max subarray
        #one where the max is in the middle of the circular subarray, so wrapping doesnt help
        #one where the max is split between the right and left sides, so wrapping helps. in order to calculate this we do the total - min subarray, as the min would be the contiguous middle part of the array
        maxSum, minSum, curMax, curMin = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            curMin = min(nums[i], curMin + nums[i])
            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
            print(f"{maxSum}, {minSum}")
        if maxSum < 0:
            return maxSum #if all elements are negative, just choose the smallest negative
        total = sum(nums)
        print(total)
        return max(maxSum, total - minSum)

        