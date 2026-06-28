class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #dfs solution, travel down a path that matches, if it doesnt match return to the original path and explore each directions
        #maybe need to mark each cell we've already visited?
        rows, cols = len(board), len(board[0])
        dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c, i):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 1 or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            tmp = board[r][c]
            board[r][c] = 1
            for dr, dc in dirs:
                if dfs(dr + r, dc + c, i + 1):
                    print(board[r][c])
                    return True
            board[r][c] = tmp
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
        
                    
            
