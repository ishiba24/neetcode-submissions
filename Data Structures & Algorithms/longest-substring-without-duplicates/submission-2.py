class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window solution, increase r each time and add to a set, when dup is detected move l and remove l from set
        charSet = set()
        l = 0
        res = 0 
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

