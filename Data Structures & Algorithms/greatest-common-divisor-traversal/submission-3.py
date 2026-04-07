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
        for i,n1 in enumerate(nums):
            for j,n2 in enumerate(nums):
                if i > j: continue
                if math.gcd(n1,n2) > 1: dsu.union(i,j)  
        return dsu.comps() == 1      