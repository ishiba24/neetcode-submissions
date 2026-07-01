class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        #thinking sorting the dictionary by length, trying the largest words first and building a try out s. then keeping track of the biggest word to fit so far
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        dp = {len(s): 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i + 1)
            cur = trie.root
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.isWord:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        return dfs(0)