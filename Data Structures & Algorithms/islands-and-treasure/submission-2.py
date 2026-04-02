class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visit = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    q.append(([r,c,0]))
                    visit.add((r,c))
        while q:
            r, c, dist = q.popleft()
            grid[r][c] = dist
            steps = [[-1,0],[1,0],[0,1],[0,-1]]
            for y, x in steps:
                nr, nc = r+y, c+x
                if min(nr,nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == -1 or (nr, nc) in visit: continue
                q.append((nr, nc, dist+1))
                visit.add((nr, nc))