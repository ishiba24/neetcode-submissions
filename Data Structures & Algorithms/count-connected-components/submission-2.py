class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    def find(self, x):
        #find the root of the current node x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xSet = self.find(x)
        ySet = self.find(y)
        if self.rank[xSet] > self.rank[ySet]:
            self.parent[ySet] = self.parent[xSet]
        elif self.rank[ySet] > self.rank[xSet]:
            self.parent[xSet] = self.parent[ySet]
        else:
            self.parent[xSet] = self.parent[ySet]
            self.rank[ySet] += 1
        



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DSU(n)
        res = set()
        for edge in edges:
            ds.union(edge[0], edge[1])
        for i in range(n):
            res.add(ds.find(i))
        return len(res)
