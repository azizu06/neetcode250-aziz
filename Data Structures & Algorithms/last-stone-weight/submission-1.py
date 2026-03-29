class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            if x != y: heapq.heappush(stones, -(max(x,y)-min(x,y)))
        return abs(stones[0]) if stones else 0