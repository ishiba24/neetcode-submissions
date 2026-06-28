class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        pref ={0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += pref.get(diff, 0)
            pref[curSum] = 1 + pref.get(curSum, 0)
        return res