class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        if self.parent[x] != x: self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x,y = self.find(x), self.find(y)
        if x == y: return False
        if self.size[x] < self.size[y]: x,y = y,x
        self.parent[y] = x
        self.size[x]+=self.size[y]
        return True
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        dsu = DSU()
        for acc in accounts:
            name, e1 = acc[0], acc[1]
            emailToName[e1] = name
            dsu.find(e1)
            for i in range(2, len(acc)):
                emailToName[acc[i]] = name
                dsu.union(e1,acc[i])
        groups = defaultdict(list)
        for email in dsu.parent:
            root = dsu.find(email)
            groups[root].append(email)
        res = []
        for k in groups:
            res.append([emailToName[k]]+sorted(groups[k]))
        return res

 
            