class Solution:
    def numDecodings(self, s: str) -> int:
        #iterate, two cases, i + 1 or i + 2. edge case is if s[i] == 0 or s[i] > 26
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)