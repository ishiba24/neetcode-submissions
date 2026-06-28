class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        res = ""
        i = 0
        for c in t:
            if c == s[i]:
                res += c
                i += 1
            if i > len(s) - 1:
                break
        return res == s