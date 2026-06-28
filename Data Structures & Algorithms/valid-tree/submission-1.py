class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False #edges must be n-1 to be valid
        adjList = [[] for i in range(n)] #builds a list of adjacencies for each node
        vis = set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        def dfs(node, parent):
            if node in vis:
                return False
            vis.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(vis) == n