class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set() #use sets to track whether queen position is valid

        res = []
        board = [["."] * n for i in range(n)] #setup board

        def backtrack(r):
            if r == n: 
                copy = ["".join(row) for row in board] #if we've iterated through all rows
                res.append(copy)
                return
            for c in range(n): #for each column in length of board
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue 
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res