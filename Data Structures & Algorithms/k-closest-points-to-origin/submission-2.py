class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = []
        for i in range(len(points)):
            dist = points[i][0]**2+points[i][1]**2
            heapq.heappush(coords, (-dist, i))
            if len(coords) > k: heapq.heappop(coords)
        res = []
        for i in range(k):
            point = heapq.heappop(coords)[1]
            res.append(points[point])
        return res