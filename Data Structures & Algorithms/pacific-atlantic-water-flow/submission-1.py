class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #top left is pacific, bottom right is atlantic. bf is calling bfs from every node, optimize by keeping track of whether a cell reaches p or a?
        rows, cols = len(heights), len(heights[0])
        dirs = [[0, 1], [1,0], [0, -1], [-1, 0]]
        def bfs(q):
            vis = set(q)
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in vis or heights[nr][nc] < heights[r][c]:
                        continue
                    vis.add((nr, nc))
                    q.append((nr, nc))
            return vis
        
        pacific = deque()
        atlantic = deque()
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        reachesPacific = bfs(pacific)
        reachesAtlantic = bfs(atlantic)
        return [[r,c] for r in range(rows) for c in range(cols) if (r, c) in reachesPacific and (r,c) in reachesAtlantic]