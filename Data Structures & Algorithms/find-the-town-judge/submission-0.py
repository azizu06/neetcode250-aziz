class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        cur = trust[0][1]
        for p, j in trust:
            if p == cur or j != cur:
                return -1
        return cur