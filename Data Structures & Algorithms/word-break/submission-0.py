class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp to remember certain branches, explore a branch at a time? if wd[i] in s[j:len(wd[i])]?
        #try to match at each index in s, then iterate back to front. if we can match at 0, can we match at 0 + i where i is the length of the match?
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w: #if theres enough space for our word and the word matches the rest of our string
                    dp[i] = dp[i + len(w)] #base case will be True at the end, so it should equal True all the way through to work.
                if dp[i]:
                    break
        return dp[0]
