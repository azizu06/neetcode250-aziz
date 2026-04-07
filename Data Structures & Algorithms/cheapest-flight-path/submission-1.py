class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))
        heap = [(0,src,-1,0)]
        visit = set()
        while heap:
            print(heap[0])
            w1,node,stop,cost = heapq.heappop(heap)
            if node in visit or stop > k: 
                visit = set()
                continue
            if node == dst: return cost
            visit.add(node)
            for nei,w2 in adj[node]:
                if nei in visit: continue
                heapq.heappush(heap,(w2,nei,stop+1,cost+w2))
        return -1
