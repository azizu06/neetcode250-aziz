class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        n = len(s)
        def dfs(i):
            if i in memo: return memo[i]
            if i == n: return 1
            if s[i] == '0': return 0
            res = dfs(i+1)
            if i < n-1 and 10 <= int(s[i:i+2]) <= 26:
                res+=dfs(i+2)
            memo[i] = res
            return res
        return dfs(0)