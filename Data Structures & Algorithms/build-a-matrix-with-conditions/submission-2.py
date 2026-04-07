class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topSort(cond):
            adj = defaultdict(list)
            indeg = defaultdict(int)
            for u,v in cond:
                adj[u].append(v)
                indeg[v]+=1
            q = deque(i for i in range(1,k+1) if not indeg[i])
            order = []
            while q:
                n = q.popleft()
                order.append(n)
                for nei in adj[n]:
                    indeg[nei]-=1
                    if not indeg[nei]: q.append(nei)
            return order
        rows = topSort(rowConditions)
        if len(rows) != k: return []
        cols = topSort(colConditions)
        if len(cols) != k: return []
        res = [[0]*k for _ in range(k)]
        points = {i: [0,0] for i in range(1,k+1)}
        for i,r in enumerate(rows):
            points[r][0] = i
        for i,c in enumerate(cols):
            points[c][1] = i
        for n,(r,c) in points.items():
            res[r][c] = n
        return res
        