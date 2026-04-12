class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1,w2 = len(word1),len(word2)
        dp = [[0]*(w1+1) for _ in range(w2+1)]
        for i in range(w1+1):
            dp[w2][i] = w1-i
        for i in range(w2+1):
            dp[i][w1] = w2-i
        for i in range(w2-1,-1,-1):
            for j in range(w1-1,-1,-1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i+1][j+1],dp[i][j+1])+1
        return dp[0][0]
            
    class Solution2:
        def minDistance(self, word1: str, word2: str) -> int:
            w1,w2 = len(word1),len(word2)
            memo = {}
            def dfs(i,j):
                if (i,j) in memo: return memo[(i,j)]
                if i == w1 and j == w2: return 0
                if j == w2: return w1-i
                if i == w1: return w2-j
                if word1[i] != word2[j]:
                    res = min(dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))+1
                else:
                    res = dfs(i+1,j+1)
                memo[(i,j)] = res
                return res
            return dfs(0,0)
            


