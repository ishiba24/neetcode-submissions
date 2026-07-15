class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #use bfs, create intermediate states of word almost like trie
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)
        vis = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in vis:
                            q.append(neiWord)
                            vis.add(neiWord)
            res += 1
        return 0