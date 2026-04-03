class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        pac, atl = set(), set()
        def dfs(r,c,visit):
            visit.add((r,c))
            for y,x in steps:
                nr,nc = r+y,c+x
                if min(nr,nc) < 0 or nr >= R or nc >= C or (nr,nc) in visit or heights[r][c] > heights[nr][nc]: continue
                dfs(nr,nc,visit)
        for r in range(R):
            dfs(r,0,pac)
            dfs(r,C-1,atl)
        for c in range(C):
            dfs(0,c,pac)
            dfs(R-1,c,atl)
        return [[r,c] for r in range(R) for c in range(C) if (r,c) in pac and (r,c) in atl]

        

        