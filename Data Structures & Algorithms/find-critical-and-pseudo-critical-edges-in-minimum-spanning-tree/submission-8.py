class DSU:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.sz = [1]*n
        self.comps = n
    def find(self,x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        x,y = self.find(x), self.find(y)
        if x == y: return False
        self.comps-=1
        if self.sz[x] < self.sz[y]: x,y = y,x
        self.sz[x]+=self.sz[y]
        self.par[y] = x
        return True
    def comp(self): return self.comps
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges): 
            e.append(i)
        edges.sort(key=lambda x:x[2])
        dsu = DSU(n)
        real = 0
        for u,v,w,_ in edges:
            if not dsu.union(u,v): continue
            real+=w
        res = [[],[]]
        for i,(u1,v1,wx,a) in enumerate(edges):
            d1,d2 = DSU(n),DSU(n)
            w1,w2 = wx,0
            d1.union(u1,v1)
            for j,(u2,v2,wy,b) in enumerate(edges):
                if i == j: continue
                if d1.union(u2,v2): w1+=wy
                if d2.union(u2,v2): w2+=wy
            if w2 > real or d2.comp() != 1: 
                res[0].append(a)
            elif w1 == real and d1.comp() == 1:
                res[1].append(a)
        return res
            



        


