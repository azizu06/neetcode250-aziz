class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (u,v) in enumerate(equations):
            adj[u].append((v,values[i]))
            adj[v].append((u, 1/values[i]))
        def dfs(src,target,val,visit):
            if src not in adj or target not in adj: return -1.0
            if src == target: return val
            for nei,num in adj[src]:
                if nei in visit: continue
                visit.add(nei)
                ans = dfs(nei,target,num*val,visit)
                if ans != -1.0: return ans
            return -1.0
        return [dfs(a,b,1.0,set([a])) for a,b in queries]
        
