class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi sourc bfs again until the queue fully empties out, start by adding each rotten fruit
        vis = set()
        q = deque()
        numOranges = 0
        def addCell(r, c):
            nonlocal numOranges
            if min(r, c) < 0 or c >= cols or r >= rows or (r, c) in vis or grid[r][c] != 1:
                return
            vis.add((r, c))
            q.append((r, c))
            numOranges -= 1
        rows, cols = len(grid), len(grid[0])
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    vis.add((r, c))
                elif grid[r][c] == 1:
                    numOranges += 1
        count = 0
        while q and numOranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    addCell(r + dr, c + dc)
            count += 1
        return count if numOranges == 0 else -1
                