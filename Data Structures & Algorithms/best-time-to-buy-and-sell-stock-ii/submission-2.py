class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total, l , r = 0, 0, 1
        while r < len(prices):
            if prices[r]-prices[l] > 0:
                total += prices[r]-prices[l]
            l, r = r, r+1
        return total
