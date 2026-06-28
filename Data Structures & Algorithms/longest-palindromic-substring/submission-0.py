class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i #odd length palindrome check
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1 #even length palindrome check 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

        #basically check each twice and run this algorithm from each position, should result in O(n^2) time