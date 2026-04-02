class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for p, j in trust:
            outdeg[p]+=1
            indeg[j]+=1
        for i in range(1, n+1):
            if indeg[i] == n-1 and not outdeg[i]:
                return i
        return -1