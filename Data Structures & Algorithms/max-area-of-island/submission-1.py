class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #do number of islands, but also keep track of the maximum size of each island
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if r < 0 or c < 0 or c >= cols or r >= rows or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            for dr, dc in dirs:
                area += dfs(dr + r, dc + c)
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res
