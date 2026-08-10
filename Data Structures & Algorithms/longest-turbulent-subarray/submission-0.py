class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #how do you check if signs are opposite? 
        #if nums[i] < nums[i + 1], then nums[i + 1] > nums[i + 2], and so on. almost like a hill
        #can still use kadanes algo to keep track of the longest likely
        if len(arr) == 1:
            return 1
        maxLen, curLen = 1, 1
        prev = '='
        for i in range(len(arr) -1):
            if arr[i] < arr[i + 1]:
                cur = '<'
            elif arr[i] > arr[i + 1]:
                cur = '>'
            else:
                cur = '='
            if cur == '=':
                curLen = 1
            elif cur != prev:
                curLen += 1
            else:
                curLen = 2
            maxLen = max(maxLen, curLen)
            prev = cur
        return maxLen