class UF:
    def __init__(self,n):
        self.comp = n
        self.parent = list(range(n))
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        uf = UF(n)
        for u,v in edges:
            if not uf.union(u,v):
                return False
        return uf.comps() == 1

            

        