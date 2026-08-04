class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #thinking at each index track whether if keeping that element as the last in s1 is true or False, and then try and include the next element.
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = {}
        targetSum = total // 2
        def dfs(i, curSum):
            if curSum == targetSum:
                dp[(i, curSum)] = True
                return True
            if curSum > targetSum:
                return False
            if i == len(nums):
                return False
            if (i, curSum) in dp:
                return dp[(i, curSum)]
            if (dfs(i + 1, curSum + nums[i])):
                dp[(i, curSum)] = True
                return True
            dp[(i, curSum)] = dfs(i + 1, curSum)
            return dp[(i, curSum)]
        return dfs(0, 0)
            
                

        