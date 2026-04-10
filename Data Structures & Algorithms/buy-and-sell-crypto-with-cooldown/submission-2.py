class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,buy):
            if i >= len(prices): return 0
            if (i,buy) in memo: return memo[(i,buy)]
            cool = dfs(i+1,buy)
            if buy:
                res = max(cool,dfs(i+1,False)-prices[i])
                memo[(i,buy)] = res
                return res
            else:
                res = max(cool,dfs(i+2,True)+prices[i])
                memo[(i,buy)] = res
                return res
        return dfs(0,True)
            
