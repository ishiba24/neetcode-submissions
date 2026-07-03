class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #try to solve with bfs
        dirs = [[1, 0], [0,1], [0, -1], [-1, 0]]
        rows, cols = len(grid), len(grid[0])
        area = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append([r, c])
            res = 1
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr >= rows or nc <0 or nc >= cols or grid[nr][nc] == 0):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1
            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area