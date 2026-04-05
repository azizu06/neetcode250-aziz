class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist = defaultdict(int)
        small = n
        for i in range(n):
            q = deque([(i,0)])
            visit = set([i])
            while q:
                n,h = q.popleft()
                for nei in adj[n]:
                    if nei in visit: continue
                    visit.add(nei)
                    q.append((nei,h+1))
            dist[i] = h
            small = min(h, small)
        return [k for k,v in dist.items() if v == small]