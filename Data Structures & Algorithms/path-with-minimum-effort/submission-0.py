class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #use dijkstras to find minimum path to travel to bottom right node?
        minHeap = [[0,0,0]]
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1], [1, 0], [0, -1], [-1, 0]]
        vis = set()
        while minHeap:
            effort, r, c = heapq.heappop(minHeap)

            if (r, c) in vis:
                continue
            vis.add((r, c))
            if (r, c) == (rows -1, cols - 1):
                return effort
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0 or nr >= rows or nc >= cols or (nr, nc) in vis):
                    continue
                newEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minHeap, [newEffort, nr, nc])
            