class UF:
    def __init__(self,n):
        self.comp = n
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self,x):
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py: return False
        self.comp-=1
        if self.size[px] < self.size[py]: px,py = py,px
        self.size[px]+=self.size[py]
        self.parent[py] = px
        return True
    
    def comps(self):
        return self.comp

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u,v in edges: uf.union(u,v)
        return uf.comps()