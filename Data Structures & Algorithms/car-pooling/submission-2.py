class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        cur = 0
        for ppl, start, end in trips:
            while heap and heap[0][0] <= start:
                _, pas = heapq.heappop(heap)
                cur-=pas
            cur+=ppl
            heapq.heappush(heap, (end, ppl))
            if cur > capacity: return False
        return True
            


# [[1,1,3],[3,2,3],[2,3,5]]