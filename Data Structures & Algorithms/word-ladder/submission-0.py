class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #create intermediate states for each word, almost like a trie. Then call BFS on each word and explore its children until endword is found
        #use a visit set to avoid duplicates
        #words with the same pattern are neighors
        visited = set([beginWord])
        q = deque([beginWord])
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:] #create each pattern
                nei[pattern].append(word) #{pattern : [word]}
        res = 1
        while q:
            for i in range(len(q)): #perform BFS
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0

        
