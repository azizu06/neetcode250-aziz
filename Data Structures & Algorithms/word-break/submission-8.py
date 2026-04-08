class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            if not dp[i]: continue
            for j in range(i,n):
                if s[i:j+1] in words:
                    dp[j+1] = True
        return dp[-1]

