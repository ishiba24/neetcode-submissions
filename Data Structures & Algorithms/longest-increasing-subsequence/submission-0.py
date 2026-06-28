class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #keep track of the LIS at each position, take max up until that point?
        #use recursion, either add or dont add the current element based on if it extends the subsequence
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)