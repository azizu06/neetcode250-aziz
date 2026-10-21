class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        steps = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        visit = {(0,0)}
        q = deque([(0,0)])
        n = len(grid)

        dist = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == n-1 and c == n-1:
                    return dist
                for dr, dc in steps:
                    nr,nc = r+dr,c+dc
                    if min(nr,nc) < 0 or nr == n or nc == n or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    q.append((nr,nc))       
                    visit.add((nr,nc))
            dist+=1
        return -1
            