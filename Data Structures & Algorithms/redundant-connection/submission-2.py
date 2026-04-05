class UF:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)
    def find(self,x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x,y = self.find(x), self.find(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y = y,x
        self.size[x]+=self.size[y]
        self.parent[y] = x
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges))
        for u,v in edges:
            if not uf.union(u,v): return [u,v]
        