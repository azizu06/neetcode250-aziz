class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i]
                heapq.heappush(heap,(end-start+1,end))
                i+=1
            while heap and q > heap[0][1]:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        return [res[q] for q in queries]

                