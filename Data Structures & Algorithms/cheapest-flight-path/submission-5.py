class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0
        for _ in range(k+1):
            t = prices.copy()
            for s,d,p in flights:
                if prices[s] != float('inf') and prices[s] + p < t[d]:
                    t[d] = prices[s]+p
            prices = t
        return -1 if prices[dst] == float('inf') else prices[dst]


