class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visit = set()
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visit or grid[r][c] == '0': return 0
            visit.add((r, c))
            steps = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for y, x in steps:
                dfs(r+y, c+x)
            return 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res+=dfs(r, c)
        return res