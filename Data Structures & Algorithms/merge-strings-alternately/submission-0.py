class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = 0
        s2 = 0
        n = len(word1)
        m = len(word2)
        res = ""
        while s1 < n and s2 < m:
            res += word1[s1]
            s1 += 1
            res += word2[s2]
            s2 += 1
        if s1 != n:
            res += word1[s1:]
        if s2 != m:
            res += word2[s2:]
        return res