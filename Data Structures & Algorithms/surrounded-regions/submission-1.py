class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R,C = len(board), len(board[0])
        visit = set()
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if min(r,c) < 0 or r >= R or c >= C or (r,c) in visit or board[r][c] == 'X': return
            visit.add((r,c))
            for y,x in steps:
                dfs(r+y,c+x)

        for r in range(R):
            dfs(r,0)
            dfs(r,C-1)
        for c in range(C):
            dfs(0,c)
            dfs(R-1,c)
        for r in range(1, R-1):
            for c in range(1, C-1):
                if (r,c) not in visit: board[r][c] = 'X'