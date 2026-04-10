class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2
        memo = {}
        def dfs(i,cur):
            if i == len(stones): return abs(cur-(total-cur))
            if (i,cur) in memo: return memo[(i,cur)]
            memo[(i,cur)] = min(dfs(i+1,cur),dfs(i+1,cur+stones[i]))
            return memo[(i,cur)]
        return dfs(0,0)
