class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit = 0, 1, 0
        while r < len(prices):
            best = prices[r] - prices[l]
            if best < 0:
                l=r
                r+=1
                continue
            profit = max(profit, best)
            r+=1
        return profit
            