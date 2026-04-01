class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cost = list(zip(capital, profits))
        profit = []
        heapq.heapify(cost)
        if w < cost[0][0]: return w
        for _ in range(k):
            while cost and w >= cost[0][0]:
                c, p = heapq.heappop(cost)
                heapq.heappush(profit, (-p, c))
            p, c = heapq.heappop(profit)
            w+=(-p)
        return w

