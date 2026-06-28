class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #need to create k subsets all of the same value
        #similar to matchstick, sum divided by k
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k
        groups = [0] * k
        nums.sort(reverse = True)
        def backtrack(i):
            if i >= len(nums):
                return True
            for group in range(k):
                if groups[group] + nums[i] <= target:
                    groups[group] += nums[i]
                    if backtrack(i + 1):
                        return True
                    groups[group] -= nums[i]
                if groups[group] == 0:
                    break
            return False
        return backtrack(0)
                    

