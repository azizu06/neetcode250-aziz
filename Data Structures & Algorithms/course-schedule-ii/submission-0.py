class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indeg = [0]*numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indeg[crs]+=1
        res = []
        q = deque([i for i in range(numCourses) if not indeg[i]])
        while q:
            crs = q.popleft()
            res.append(crs)
            for nei in adj[crs]:
                indeg[nei]-=1
                if not indeg[nei]: q.append(nei)
        return res if len(res) == numCourses else []