class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #iterate through, adding max of sliding window to res at each step? increment l at each position
        res = []
        l = 0
        curWindow = []
        for i in range(k):
            curWindow.append(nums[i])
        res.append(max(curWindow))
        l += 1
        for r in range(k, len(nums)):
            curWindow.append(nums[r])
            curWindow.pop(0)
            l += 1
            res.append(max(curWindow))
        return res