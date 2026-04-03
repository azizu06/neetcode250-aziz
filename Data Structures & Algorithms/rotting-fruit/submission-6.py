class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c,0))
        if not fresh: return 0
        while q:
            r,c,dist = q.popleft()
            steps = [(1,0),(-1,0),(0,1),(0,-1)]
            for y, x in steps:
                nr, nc = r+y, c+x
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    q.append((nr,nc,dist+1))
                    fresh-=1
                    grid[nr][nc] = 2
                    if not fresh: return dist+1
        return -1