class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q, visit = deque(), set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]: fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c,0))
                    visit.add((r,c))
        if not fresh: return 0
        while q:
            r,c,dist = q.popleft()
            if grid[r][c]: fresh-=1
            if not fresh: return dist
            steps = [(1,0),(-1,0),(0,1),(0,-1)]
            for y, x in steps:
                nr, nc = r+y, c+x
                if min(nr,nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or (nr,nc) in visit or not grid[nr][nc]: continue
                q.append((nr,nc,dist+1))
                visit.add((nr,nc))
        return -1