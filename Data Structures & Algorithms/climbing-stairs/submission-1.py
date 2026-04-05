class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if not n: return 1
            if n < 0: return 0
            if n in memo: return memo[n]
            res = dfs(n-1)+dfs(n-2)
            memo[n] = res
            return res
        return dfs(n)