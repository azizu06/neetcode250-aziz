class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        heap = [(grid[0][0],0,0)]
        visit = set()
        res = 0
        while heap:
            t,r,c = heapq.heappop(heap)
            if (r,c) in visit: continue
            visit.add((r,c))
            res = max(res,t)
            if r == c == n-1: return res
            for dr,dc in direc:
                nr,nc = r+dr,c+dc
                if min(nr,nc) < 0 or max(nr,nc) >= n or (nr,nc) in visit: continue
                heapq.heappush(heap,(grid[nr][nc],nr,nc))
