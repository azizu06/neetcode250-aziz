class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        n,m = len(s),len(p)
        def dfs(i,j):
            if j == m: return i == n
            if (i,j) in dp: return dp[(i,j)]
            match = i < n and (s[i] == p[j] or p[j] == '.')
            if j+1 < m and p[j+1] == '*':
                res = dfs(i,j+2) or (match and dfs(i+1,j))
            else: 
                res = match and dfs(i+1,j+1)
            dp[(i,j)] = res
            return res

        return dfs(0,0)
