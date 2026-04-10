class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total//2
        dp = [0]*(target+1)
        for s in stones:
            for i in range(target,-1,-1):
                if i < s: continue
                dp[i] = max(dp[i],dp[i-s]+s)
        return total-2*dp[target]
