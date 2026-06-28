class Solution:
    #use a disjoint set union to keep track of which nodes have been visisted, sort the edges by ascending order to always take the min amt, and perform kruskals
    class DSU:
            def __init__(self, n):
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
                    return False #dont merge, alr in same group
                if self.size[pu] < self.size[pv]:
                    self.parent[pu] = pv
                    self.size[pv] += self.size[pu]
                else:
                    self.parent[pv] = pu
                    self.size[pu] += self.size[pv]
                return True
            
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #find the shortest weighted path between nodes so that that everything is connected, looks like an MST. kruskals
        n = len(points)
        dsu = self.DSU(n)
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res