class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        prev = cur = 1
        res = 0
        for i in range(2,n+1):
            res = prev+cur
            prev, cur = cur, res
        return res
