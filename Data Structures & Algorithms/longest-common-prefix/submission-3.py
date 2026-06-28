class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #iterate through each string, while still equal continue, when not return
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
            

