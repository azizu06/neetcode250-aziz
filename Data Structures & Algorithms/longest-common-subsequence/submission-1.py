class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[j-1] == t[i-1]: 
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[m][n]