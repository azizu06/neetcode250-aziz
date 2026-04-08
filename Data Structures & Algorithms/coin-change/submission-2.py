class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] == amount+1: continue
            for c in coins:
                if i + c > amount: continue
                dp[i+c] = min(dp[i+c],dp[i]+1)
        return -1 if dp[-1] == amount+1 else dp[-1]
