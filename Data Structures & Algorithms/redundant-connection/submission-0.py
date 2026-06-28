class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #use union find to locate the edge that doesnt belong?
        #cycle detection problem, n nodes, n - 1 edges ALWAYS if no cycle.if edges = nodes, cycle
        #union find will auto detect the last edge in the graph when using it
        #union find on each edge, and if the edge is already found(have same parent), return that edge
        n = len(edges)
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1) 
        def find(n1):
            res = n1
            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            res1, res2 = find(n1), find(n2)
            if res1 == res2:
                return True
            if rank[res1] < rank[res2]:
                par[res1] = res2
                rank[res2] += rank[res1]
            else:
                par[res2] = res1
                rank[res1] += rank[res2]
            return False
        for i, j in edges:
            if union(i, j):
                return [i, j]

