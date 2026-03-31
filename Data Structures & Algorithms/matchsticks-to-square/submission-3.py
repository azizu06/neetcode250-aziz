class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        target = sum(matchsticks)/4
        def dfs(i, sides):
            if i == len(matchsticks):
                for i in range(4):
                    if sides[i] != target: return False
                return True
            for j in range(4):
                if sides[j]+matchsticks[i] > target: continue
                sides[j]+=matchsticks[i]
                if dfs(i+1, sides): return True
                sides[j]-=matchsticks[i]
            return False
        return dfs(0, [0]*4)