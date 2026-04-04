class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [False]*len(queries)
        if not prerequisites: return res
        adj = [[] for i in range(numCourses)]
        for pre,crs in prerequisites:
            adj[pre].append(crs)
        for i, (pre,target) in enumerate(queries):
            visit = set([pre])
            q = deque([pre])
            while q:
                crs = q.popleft()
                if crs == target:
                    res[i] = True
                    break
                for nei in adj[crs]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
        return res