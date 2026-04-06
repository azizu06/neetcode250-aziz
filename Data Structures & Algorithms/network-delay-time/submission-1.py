class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        visit = set()
        res = 0
        heap = [[0,k]]
        while heap:
            w,node = heapq.heappop(heap)
            if node in visit: continue
            visit.add(node)
            res = max(res,w)
            if len(visit) == n: return res
            for nei,time in adj[node]:
                heapq.heappush(heap,(time+w,nei))
        return -1