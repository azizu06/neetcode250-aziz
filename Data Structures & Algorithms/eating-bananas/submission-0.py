class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = 0
        for p in piles:
            maxPile = max(maxPile, p)
        minSpeed = float('inf')
        l, r = 1, maxPile
        while l <= r:
            time = 0
            mid = (l+r)//2
            for p in piles:
                time += math.ceil(p/mid)
            if time <= h:
                minSpeed = min(mid, minSpeed)
                r = mid-1
            else:
                l = mid+1
        return minSpeed
            

