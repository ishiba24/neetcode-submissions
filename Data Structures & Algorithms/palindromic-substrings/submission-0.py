class Solution:
    def countSubstrings(self, s: str) -> int:
        #count the number of palindromes, use DP to track already completed?
        #each element is a palindrome
        #similar to longest palindrome

        res = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
        