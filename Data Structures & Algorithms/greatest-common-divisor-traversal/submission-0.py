class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        self.n -= 1
        if self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True
    def isConnected(self):
        return self.n == 1
        
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #another kahns algo/topological sort type of question, but you can only reach the next index by finding a path where the gcd > 1?
        ds = DSU(len(nums))
        factorIndex = {}
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factorIndex:
                        ds.union(i, factorIndex[f])
                    else:
                        factorIndex[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factorIndex:
                    ds.union(i, factorIndex[n])
                else:
                    factorIndex[n] = i
        return ds.isConnected()