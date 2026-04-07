class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))
        heap = [(0,src,-1)]
        while heap:
            w1,node,stop = heapq.heappop(heap)
            if stop > k: continue
            if node == dst: return w1
            for nei,w2 in adj[node]:
                heapq.heappush(heap,(w1+w2,nei,stop+1))
        return -1
