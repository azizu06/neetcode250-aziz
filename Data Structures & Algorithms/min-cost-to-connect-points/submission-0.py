class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)  
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                cost = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[tuple(points[i])].append((points[j],cost))
                adj[tuple(points[j])].append((points[i],cost))
        heap = [(0,points[0])]
        visit = set()
        res = 0
        while heap:
            w,p = heapq.heappop(heap)
            p = tuple(p)
            if p in visit: continue
            visit.add(p)
            res+=w
            for nei,dist in adj[p]:
                if tuple(nei) in visit: continue
                heapq.heappush(heap,(dist,nei))
        return res

        