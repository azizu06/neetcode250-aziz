class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        def canPlace(r, c):
            for i in range(r+1, n):
                if board[i][c] != '.': return False
            for i in range(r-1, -1, -1):
                if board[i][c] != '.': return False
            i, j = r+1, c-1
            while j >= 0 and i < n:
                if board[i][j] != '.': return False
                i, j = i+1, j-1
            i, j = r-1, c-1
            while j >= 0 and i >= 0:
                if board[i][j] != '.': return False
                i, j = i-1, j-1
            i, j = r+1, c+1
            while j < n and i < n:
                if board[i][j] != '.': return False
                i, j = i+1, j+1
            i, j = r-1, c+1
            while j < n and i >= 0:
                if board[i][j] != '.': return False
                i, j = i-1, j+1
            return True
            
        def dfs(i, r, c):
            nonlocal board
            if i == n: 
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if not canPlace(r, c): continue
                board[r][c] = 'Q'
                dfs(i+1, r+1, c)
                board[r][c]= '.'
            
        dfs(0, 0, 0)
        return res
