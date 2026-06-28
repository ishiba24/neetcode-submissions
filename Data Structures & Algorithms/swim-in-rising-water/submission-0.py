class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #gotta be some time of dfs, maybe compare the values to see if they're less than each other and increment time t?, 
        #use dijkstras because the max grid value equals the amount of time it takes, so we need to minimize this max(aka find the shortest path between two nodes)
        n = len(grid)
        vis = set()
        minHeap = [[grid[0][0], 0 , 0]] #push the top left node, its row and col
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        vis.add((0,0))
        while minHeap:
            time, row, col = heapq.heappop(minHeap)
            if row == n - 1 and col == n - 1:
                return time #reached the bottom right
            for dr, dc in directions:
                neiR, neiC = row + dr, col + dc
                if (neiR < 0 or neiC < 0 or neiR == n or neiC == n or (neiR, neiC) in vis):
                    continue
                vis.add((neiR, neiC))
                heapq.heappush(minHeap, [max(time, grid[neiR][neiC]), neiR, neiC]) #time is continuously updated to be the max value along the path.

