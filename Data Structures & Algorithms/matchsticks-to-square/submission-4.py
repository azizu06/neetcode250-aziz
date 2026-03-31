class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total%4: return False
        target = total//4
        sides = [0]*4
        def dfs(i):
            if i == len(matchsticks): return True
            for j in range(4):
                if sides[j]+matchsticks[i] > target: continue
                sides[j]+=matchsticks[i]
                if dfs(i+1): return True
                sides[j]-=matchsticks[i]
                if not sides[j]: break
            return False
        return dfs(0)