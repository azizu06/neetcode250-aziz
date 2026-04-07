class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0]*k for _ in range(k)]
        adjRow,adjCol = defaultdict(list),defaultdict(list)
        inRow,inCol = defaultdict(int),defaultdict(int)
        for u,v in rowConditions:
            adjRow[u].append(v)
            inRow[v]+=1
        for u,v in colConditions:
            adjCol[u].append(v)
            inCol[v]+=1
        q = deque(i for i in range(1,k+1) if not inRow[i])
        rows = []
        while q:
            n = q.popleft()
            rows.append(n)
            for nei in adjRow[n]:
                inRow[nei]-=1
                if not inRow[nei]: q.append(nei)
        if len(rows) != k: return []
        q = deque(i for i in range(1,k+1) if not inCol[i])
        cols = []
        while q:
            n = q.popleft()
            cols.append(n)
            for nei in adjCol[n]:
                inCol[nei]-=1
                if not inCol[nei]: q.append(nei)
        if len(cols) != k: return []
        points = {i: [0,0] for i in range(1,k+1)}
        for i,r in enumerate(rows):
            points[r][0] = i
        for i,c in enumerate(cols):
            points[c][1] = i
        for n,(r,c) in points.items():
            res[r][c] = n
        return res
            

        

        
        