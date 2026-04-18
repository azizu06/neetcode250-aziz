class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = {n:0}
        def dfs(i):
            if i in memo: return memo[i]
            res = float('inf')
            res = min(res,dfs(i+1)+costs[0])
            j = i
            while j < n and days[j] <= days[i]+6:
                j+=1
            res = min(res,dfs(j)+costs[1])
            j = i
            while j < n and days[j] <= days[i]+29:
                j+=1
            res = min(res,dfs(j)+costs[2])
            memo[i] = res
            return res
        return dfs(0)


"""
[1,4,6,7,8,20]

[2,7,15]
"""