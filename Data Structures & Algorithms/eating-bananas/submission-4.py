class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m, t = (l+r)//2, 0
            for p in piles:
                t += math.ceil(p/m)
            if t <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res
