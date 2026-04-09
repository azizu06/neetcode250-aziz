class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {1:1}
        def dfs(i):
            if i in memo: return memo[i]
            res = 0
            for j in range(1,i):
                res = max(res,j*(i-j),j*dfs(i-j))
            memo[i] = res
            return res
        return dfs(n)