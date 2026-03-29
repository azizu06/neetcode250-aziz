class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = []
        for i in range(len(points)):
            dist = ((points[i][0]-0)**2+(points[i][1]-0)**2)**0.5
            coords.append([dist, i])
        heapq.heapify(coords)
        res = []
        for i in range(k):
            res.append(points[heapq.heappop(coords)[1]])
        return res