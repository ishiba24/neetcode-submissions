class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        par = [i for i in range(len(isConnected))]
        n = len(isConnected)
        rank = [1] * n
        def find(p1):
            n1 = p1
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        def union(p1, p2):
            res1, res2 = find(p1), find(p2)
            if res1 == res2:
                return 0
            if rank[res1] > rank[res2]:
                par[res2] = res1
                rank[res1] += rank[res2]
            else:
                par[res1] = res2
                rank[res2] += rank[res1]
            return 1
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    count -= union(i, j)
        return count