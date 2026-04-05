class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (u,v) in enumerate(equations):
            adj[u].append((v,values[i]))
            adj[v].append((u, 1/values[i]))
        def dfs(node,target,val):
            if node == target: return val
            for nei,num in adj[node]:
                if nei in visit: continue
                visit.add(nei)
                ans = dfs(nei,target,num*val)
                if ans != -1.0: return ans
            return -1.0
        res = []
        for a,b in queries:
            if a not in adj or b not in adj:
                res.append(-1.0)
            elif a == b: 
                res.append(1.0)
            else:
                visit = set([a])
                res.append(dfs(a,b,1.0))
        return res

        
