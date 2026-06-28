class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        #expand r until it contains all letters of t
        #shrink l while it is still valid
        #how to track freq?
        #keep need and have, still do freq idea
        freqT = defaultdict(int)
        for i in range(len(t)):
            freqT[t[i]] += 1
        freqS = defaultdict(int)
        res = ''
        l = 0
        need = len(freqT)
        have = 0
        resLen = float('inf')
        for r in range(len(s)):
            freqS[s[r]] += 1
            if s[r] in freqT and freqS[s[r]] == freqT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l: r + 1]
                freqS[s[l]] -= 1
                if s[l] in freqT and freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        return res
