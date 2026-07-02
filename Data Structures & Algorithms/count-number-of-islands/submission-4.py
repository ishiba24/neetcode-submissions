class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #inc island with dfs, when you reach a point and no other point can be explored
        #mark cells that we visit with 0, sinking as we go
        res = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return 
            grid[r][c] = '0'
            for dr, dc in dirs:
                dfs(dr + r, dc + c)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res

            