class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two hashmaps of the counts, then iterate through the keys to see if they're the same
        if len(s) != len(t):
            return False
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for i in range(len(s)):
            hash1[s[i]] += 1
            hash2[t[i]] += 1
        for key in hash1:
            if hash2[key] != hash1[key]:
                return False
        return True