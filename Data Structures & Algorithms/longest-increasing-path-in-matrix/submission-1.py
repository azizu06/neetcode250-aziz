class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        indeg = defaultdict(int)
        R,C = len(matrix),len(matrix[0])
        direc = [(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(R):
            for c in range(C):
                for dr,dc in direc:
                    nr,nc = r+dr,c+dc
                    if min(nr,nc) < 0 or nr >= R or nc >= C or matrix[r][c] >= matrix[nr][nc]: continue
                    indeg[(nr,nc)]+=1
        q = deque()
        for r in range(R):
            for c in range(C):
                if not indeg[(r,c)]: q.append((r,c,1))
        res = 0
        while q:
            r,c,dist = q.popleft()
            res = max(res,dist)
            for dr,dc in direc:
                nr,nc = r+dr,c+dc
                if min(nr,nc) < 0 or nr >= R or nc >= C or matrix[r][c] >= matrix[nr][nc]: continue
                indeg[(nr,nc)]-=1
                if not indeg[(nr,nc)]: q.append((nr,nc,dist+1))
        return res



