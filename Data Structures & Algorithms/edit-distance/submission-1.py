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
            

