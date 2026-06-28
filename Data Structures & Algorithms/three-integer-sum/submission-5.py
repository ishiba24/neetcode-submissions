class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #lock one var, then two pointer on other two? need to sort first
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if i + 1 > len(nums) - 2:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum > 0:
                    k -= 1
                elif curSum < 0:
                    j += 1
                elif curSum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return res