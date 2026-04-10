class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        dp = [[float('inf')]*(c+1) for _ in range(r+1)]
        dp[r-1][c-1] = grid[r-1][c-1]
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if i == r-1 and j == c-1: continue
                dp[i][j] = grid[i][j] + min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]