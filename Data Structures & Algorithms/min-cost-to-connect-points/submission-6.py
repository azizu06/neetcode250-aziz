class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0,0)]
        visit = set()
        n,res = len(points),0
        while len(visit) < n:
            w,i = heapq.heappop(heap)
            if i in visit: continue
            visit.add(i)
            res+=w
            for j in range(n):
                if j in visit: continue
                dist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(heap,(dist,j))
        return res

        