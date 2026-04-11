class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        n = len(piles)
        suf = [0]*n
        suf[-1] = piles[-1]
        for i in range(n-2,-1,-1):
            suf[i] = piles[i]+suf[i+1]
        def dfs(i,m):
            if i == n: return 0
            if (i,m) in memo: return memo[(i,m)]
            res = 0
            for j in range(i,min(n,(2*m)+i)):
                res = max(res,suf[i]-dfs(j+1,max(m,j-i+1)))
            memo[(i,m)] = res
            return res
        return dfs(0,1)