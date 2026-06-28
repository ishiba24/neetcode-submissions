class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #check every pos with dfs to see if it connects to a border, if so dont change it. start from border and move out marking temp
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O"):
                return
            board[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        

