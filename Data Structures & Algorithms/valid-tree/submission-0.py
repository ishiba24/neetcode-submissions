class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #try to detect a cycle, and see if every node can reach another node
        if len(edges) != (n - 1):
            return False
        vis = set()
        adjList = [[] for i in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, parent):
            if node in vis:
                return False
            vis.add(node)
            for nei in adjList[node]:
                if nei == parent: #since its undirected, need to check instead of false cycles
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(vis) == n
            