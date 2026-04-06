class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R,C = len(heights), len(heights[0])
        heap = [[0,0,0]]
        visit = set()
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            best,r,c = heapq.heappop(heap)
            if (r,c) in visit: continue
            visit.add((r,c))
            if r == R-1 and c == C-1: return best
            for y,x in steps:
                nr,nc = r+y,c+x
                if min(nr,nc) < 0 or nr >= R or nc >= C or (nr,nc) in visit: continue
                diff = abs(heights[r][c]-heights[nr][nc])
                newBest = max(diff,best)
                heapq.heappush(heap,(newBest,nr,nc))

