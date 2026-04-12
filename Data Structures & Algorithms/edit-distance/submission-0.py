class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1,w2 = len(word1),len(word2)
        memo = {}
        def dfs(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if i == w1 and j == w2: return 0
            if j == w2: return w1-i
            if i == w1: return w2-j
            res = 0
            if word1[i] != word2[j]:
                res+=min(dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))+1
            else:
                res+=dfs(i+1,j+1)
            memo[(i,j)] = res
            return res
        return dfs(0,0)
            

