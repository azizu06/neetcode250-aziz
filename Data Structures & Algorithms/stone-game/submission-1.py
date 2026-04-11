class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if i == j: return 0
            res = 0
            if piles[i] < piles[j]:
                res = piles[j]+dfs(i,j-1)
            elif piles[i] > piles[j]:
                res = piles[j]+dfs(i+1,j)
            else:
                res = max(piles[j]+dfs(i,j-1),piles[i]+dfs(i+1,j))
            memo[(i,j)] = res
            return res
        return dfs(0,len(piles)-1) > 0
