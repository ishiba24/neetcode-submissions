class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multi source bfs? if at the end there are any fruit still in, return -1
        #look through and append all 2's, call bfs on each direction and keep a minute counter and how many fresh oranges
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        fresh -=1
                        q.append((row, col))
                        grid[row][col] = 2
            time += 1
        return time if fresh == 0 else -1

        

