class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u]+=1
            indeg[v]+=1
        q = deque(i for i in range(n) if indeg[i] == 1)
        while n > 2:
            sz = len(q)
            n-=sz
            for _ in range(sz):
                node = q.popleft()
                for nei in adj[node]:
                    indeg[nei]-=1
                    if indeg[nei] == 1:
                        q.append(nei)
        return list(q)