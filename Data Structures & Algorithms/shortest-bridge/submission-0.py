class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        n = len(grid)
        q = deque()
        def dfs(r,c):
            if min(r,c) < 0 or max(r,c) == n or grid[r][c] != 1: return
            grid[r][c] = 2
            q.append((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        found = False
        for r in range(n):
            if found: break
            for c in range(n):
                if not grid[r][c]: continue
                dfs(r,c)
                found = True
                break
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc
                    if min(nr,nc) < 0 or max(nr,nc) == n: continue
                    if grid[nr][nc] == 1: return dist
                    if not grid[nr][nc]:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            dist+=1