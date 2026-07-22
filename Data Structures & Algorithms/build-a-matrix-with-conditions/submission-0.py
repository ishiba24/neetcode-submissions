class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order_rows = self.topo_sort(rowConditions, k)
        order_cols = self.topo_sort(colConditions, k)
        if not order_rows or not order_cols:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_cols[j]:
                    matrix[i][j] = order_rows[i]
        return matrix






    def topo_sort(self, edges, n):
        adj = [[] for _ in range(n + 1)]
        indegrees = [0] * (n + 1)
        order = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1
        q = deque()
        for i in range(1, n + 1):
            if indegrees[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            order.append(node)
            n -= 1
            for nei in adj[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        if n != 0:
            return []
        return order
        