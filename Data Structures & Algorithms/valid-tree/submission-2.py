class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        if not edges: return True
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(node):
            visit.add(node)
            sz=1
            for nei in adj[node]:
                if nei not in visit:
                    sz+=dfs(nei)
            return sz
        for node in adj:
            if dfs(node) == n: return True
        return False
            

        