class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c]: continue
                res+=4
                steps = [[-1,0], [1, 0], [0, 1], [0, -1]]
                for y, x in steps:
                    nr, nc = r+y, c+x
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols: continue
                    if grid[nr][nc]: res-=1
        return res