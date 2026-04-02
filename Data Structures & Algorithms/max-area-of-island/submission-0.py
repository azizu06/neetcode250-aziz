class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or not grid[r][c]: return 0
            grid[r][c] = 0
            sz = 1
            steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for y, x in steps:
                sz+=dfs(r+y, c+x)
            return sz
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]: 
                    res = max(res, dfs(r, c))           
        return res