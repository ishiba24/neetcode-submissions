class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #use reverse dfs, see which points can the oceans flow into. rep them w set
        pacific = set()
        res = []
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) #top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c]) #bottom row
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0]) #left col
            dfs(r, cols - 1, atlantic, heights[r][cols - 1]) #right col
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res

