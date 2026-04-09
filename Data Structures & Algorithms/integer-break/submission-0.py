class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i < 1: return 1
            if i in memo: return memo[i]
            res = 0
            for j in range(1,i):
                res = max(res,j*(i-j),j*dfs(i-j))
            memo[i] = res
            return res
        return dfs(n)

            
            

"""
(12,1)->(6,2)->(4,3)->(3,4)->(2,6)->(1,12)
"""
