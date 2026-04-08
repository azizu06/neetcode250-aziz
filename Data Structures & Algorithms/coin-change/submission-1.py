class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort(reverse=True)
        def dfs(target,coins):
            if target in memo: return memo[target]
            if not target: return 0
            if target < 0: return float('inf')
            res = float('inf')
            for c in coins:
                nCoins = 1+dfs(target-c,coins)
                res = min(nCoins,res)
            memo[target] = res
            return res
        res = dfs(amount,coins)
        return res if res != float('inf') else -1