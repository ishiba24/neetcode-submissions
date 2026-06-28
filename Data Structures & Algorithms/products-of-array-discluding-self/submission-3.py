class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * len(nums)
        pref = [0] * len(nums)
        suff = [0] * len(nums)

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]
        for i in range(n):
            output[i] = suff[i] * pref[i]
        return output