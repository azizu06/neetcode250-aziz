class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return 0
        r,c = len(grid),len(grid[0])
        dp = [[0]*(c+1) for _ in range(r+1)]
        dp[1][1] = 1
        for i in range(1,r+1):
            for j in range(1,c+1):
                if grid[i-1][j-1]: continue
                dp[i][j]+=dp[i-1][j]+dp[i][j-1]
        return dp[r][c]
        
        