class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xSet = self.find(x)
        ySet = self.find(y)
        if xSet == ySet:
            return False
        if self.rank[xSet] > self.rank[ySet]:
            self.parent[ySet] = self.parent[xSet]
        elif self.rank[ySet] > self.rank[xSet]:
            self.parent[xSet] = ySet
        else:
            self.parent[xSet] = ySet
            self.rank[ySet] += 1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #do union find to determine the parent node, then see if a current edge already matches a parent, we can disconnect it
        ds = DSU(len(edges) + 1)
        for edge in edges:
            if not ds.union(edge[0], edge[1]):
                return edge
        
