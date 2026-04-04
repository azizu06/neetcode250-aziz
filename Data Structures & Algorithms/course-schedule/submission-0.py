class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for u,v in prerequisites:
            graph[v].append(u)
            indeg[u]+=1
        q = deque([i for i in range(numCourses) if not indeg[i]])
        res = 0
        while q:
            course = q.popleft()
            res+=1
            for nei in graph[course]:
                indeg[nei]-=1
                if not indeg[nei]: q.append(nei)
        return res == numCourses