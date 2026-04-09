class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while j*j <= n:
                if i+(j*j) > n: break
                dp[i+(j*j)] = min(dp[i+(j*j)],1+dp[i])
                j+=1
        return dp[n]