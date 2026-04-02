class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(r,c):
            q = deque([(r,c,0)])
            visit = set([(r,c)])
            while q:
                R, C, dist = q.popleft()
                if not grid[R][C]:
                    grid[r][c] = dist
                    return
                steps = [[-1,0],[1,0],[0,1],[0,-1]]
                for y, x in steps:
                    nr, nc = R+y, C+x
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == -1 or (nr, nc) in visit: continue
                    q.append((nr, nc, dist+1))
                    visit.add((nr,nc))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2147483647:
                    bfs(r,c)