class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #same as numislands, but keep track of maxArea and area
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0):
                return 0
            grid[r][c] = 0 
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)
        return maxArea