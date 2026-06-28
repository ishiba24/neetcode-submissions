class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window, if we see a duplicate character, then we increase l until no longer duplicate
        #then keep the highest length so far
        l = 0 
        res = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res