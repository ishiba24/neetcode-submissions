class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #at each point either include the next letter if it matches the first, so do we need two pointers? or we keep track if
        #the past was a palindrome and then just look up the first letter and compare it to the last
        #at each point continue the pal check, or start a new one
        res, part = [], []
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            if self.isPali(s, j, i):
                part.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                part.pop()
            dfs(j, i + 1) #try to extend the current palindrome
        dfs(0, 0)
        return res
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

