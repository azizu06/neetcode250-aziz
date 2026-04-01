class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        def canPlace(r, c):
            for i in range(r-1, -1, -1):
                if board[i][c] != '.': return False
            i, j = r-1, c-1
            while j >= 0 and i >= 0:
                if board[i][j] != '.': return False
                i, j = i-1, j-1
            i, j = r-1, c+1
            while j < n and i >= 0:
                if board[i][j] != '.': return False
                i, j = i-1, j+1
            return True
            
        def dfs(i):
            nonlocal board
            if i == n: 
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if not canPlace(i, c): continue
                board[i][c] = 'Q'
                dfs(i+1)
                board[i][c]= '.'
        dfs(0)
        return res
