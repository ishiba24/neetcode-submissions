class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #if we reach an obstacle, skip it, and if we will just add the value regardless because it would be 0. can just modify obstacleGrid[2] to be however many paths go through it
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if obstacleGrid[r][c] == -1:
                    continue
                if r == 0 or obstacleGrid[r-1][c] == -1:
                    obstacleGrid[r][c] = obstacleGrid[r][c - 1]
                    continue
                if c == 0 or obstacleGrid[r][c-1] == -1:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c]
                    continue
                obstacleGrid[r][c] = obstacleGrid[r][c-1] + obstacleGrid[r-1][c]
        return obstacleGrid[rows - 1][cols - 1] if obstacleGrid[rows - 1][cols - 1] != -1 else 0
                    