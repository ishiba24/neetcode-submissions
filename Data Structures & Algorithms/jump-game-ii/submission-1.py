class Solution:
    def jump(self, nums: List[int]) -> int:
        #maintain l and r pointers, which keep track of the farthest index that can be reached with the current range
        l, r = 0, 0 
        res = 0
        while r < len(nums) - 1:
            furthestIndex = 0
            for i in range(l, r + 1):
                furthestIndex = max(furthestIndex, i + nums[i])
            l = r + 1
            r = furthestIndex
            res += 1
        return res

