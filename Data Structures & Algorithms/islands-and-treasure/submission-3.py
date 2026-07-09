class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        #multi source bfs, need to also append a distance value
        rows, cols = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        vis = set()
        def addCell(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == -1 or (r, c) in vis:
                return
            vis.add((r, c))
            q.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    vis.add((r, c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in dirs:
                    addCell(r + dr, c + dc)
            dist += 1
    