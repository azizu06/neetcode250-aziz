class DSU:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.sz = [1]*n
        self.comp = n
    def find(self,x):
        if self.par[x] != x: self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        x,y = self.find(x),self.find(y)
        if x == y: return False
        self.comp-=1
        if self.sz[x] < self.sz[y]: x,y = y,x
        self.sz[x]+=self.sz[y]
        self.par[y] = x
        return True
    def comps(self): return self.comp
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        dsu = DSU(len(nums))
        factor = {}
        for i,n in enumerate(nums):
            f = 2
            while f*f <= n:
                if not n%f:
                    if f in factor: 
                        dsu.union(i,factor[f]) 
                    else:
                        factor[f] = i
                    while not n%f:
                        n//=f
                f+=1
            if n > 1:
                if n in factor:
                    dsu.union(i,factor[n])
                else:
                    factor[n] = i
        return dsu.comps() == 1      