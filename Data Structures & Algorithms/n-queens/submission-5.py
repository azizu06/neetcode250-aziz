class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        col, pos, neg = set(), set(), set()
        def dfs(r):
            nonlocal board
            if r == n: 
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg: continue
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c]= '.'
        dfs(0)
        return res
