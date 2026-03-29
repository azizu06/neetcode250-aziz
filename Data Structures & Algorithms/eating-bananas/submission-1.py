class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minSpeed = r
        while l <= r:
            time = 0
            mid = (l+r)//2
            for p in piles:
                time += math.ceil(p/mid)
                if time > h:
                    break
            if time <= h:
                minSpeed = mid
                r = mid-1
            else:
                l = mid+1
        return minSpeed
            

