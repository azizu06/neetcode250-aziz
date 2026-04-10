class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        dp = [float('inf')]*(c+1)
        dp[c-1] = 0
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                dp[j] = grid[i][j] + min(dp[j],dp[j+1])
        return dp[0]