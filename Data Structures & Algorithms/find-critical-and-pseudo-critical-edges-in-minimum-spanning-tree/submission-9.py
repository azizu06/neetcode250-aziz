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
        mst = 0
        for u,v,w,_ in edges:
            if not dsu.union(u,v): continue
            mst+=w
        crit, pseu = [],[]
        for u1,v1,w1,i in edges:
            d1,d2 = DSU(n),DSU(n)
            mst1,mst2 = w1,0
            d1.union(u1,v1)
            for u2,v2,w2,j in edges:
                if i == j: continue
                if d1.union(u2,v2): mst1+=w2
                if d2.union(u2,v2): mst2+=w2
            if mst2 > mst or d2.comp() != 1: 
                crit.append(i)
            elif mst1 == mst and d1.comp() == 1:
                pseu.append(i)
        return [crit,pseu]
            



        


