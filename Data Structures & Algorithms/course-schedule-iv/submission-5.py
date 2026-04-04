class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        isreq = [set() for _ in range(numCourses)]
        indeg = [0]*numCourses
        for u,v in prerequisites:
            adj[u].append(v)
            indeg[v]+=1
        q = deque([i for i in range(numCourses) if not indeg[i]])
        while q:
            node = q.popleft()
            for nei in adj[node]:
                isreq[nei].add(node)
                isreq[nei].update(isreq[node])
                indeg[nei]-=1
                if not indeg[nei]: q.append(nei)
        return [u in isreq[v] for u,v in queries]