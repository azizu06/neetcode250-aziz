class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,t = len(s1),len(s2),len(s3)
        if m+n != t: return False
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        memo = {}
        def dfs(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if i >= n: return s2[j:] == s3[i+j:]
            if j >= m: return s1[i:] == s3[i+j:]
            if i == n and j == m: return True
            res = False
            if i < n and s1[i] == s3[i+j]: res = res or dfs(i+1,j)
            if j < m and s2[j] == s3[i+j]: res = res or dfs(i,j+1)
            memo[(i,j)] = res
            return res
        return dfs(0,0)

        