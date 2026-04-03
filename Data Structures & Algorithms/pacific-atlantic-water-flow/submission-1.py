class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        def dfs(r,c,visit):
            steps = [(1,0),(-1,0),(0,1),(0,-1)]
            for y,x in steps:
                nr,nc = r+y,c+x
                if min(nr,nc) < 0 or nr >= R or nc >= C or (nr,nc) in visit or heights[r][c] > heights[nr][nc]: continue
                visit.add((nr,nc))
                dfs(nr,nc,visit)
        pac, atl = [], []
        p, a = set(), set()
        for r in range(R):
            pac.append([r,0])
            p.add((r,0))
            atl.append([r,C-1])
            a.add((r,C-1))
        for c in range(C):
            pac.append([0,c])
            p.add((0,c))
            atl.append([R-1,c])
            a.add((R-1,c))
        for r,c in pac:
            dfs(r,c,p)
        for r,c in atl:
            dfs(r,c,a)
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in p and (r,c) in a:
                    res.append([r,c])
        return res

        

        