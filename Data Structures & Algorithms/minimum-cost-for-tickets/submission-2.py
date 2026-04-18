class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {len(days):0}
        def dfs(i):
            if i in memo: return memo[i]
            j = i
            res = float('inf')
            for k,d in enumerate([1,7,30]):
                while j < len(days) and days[j] < days[i]+d:
                    j+=1
                res = min(res,dfs(j)+costs[k])
            memo[i] = res
            return res
        return dfs(0)