class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, minSpeed = 1, max(piles), max(piles)
        while l <= r:
            time, speed = 0, (l+r)//2
            for p in piles:
                time += math.ceil(p/speed)
            if time <= h:
                minSpeed, r = speed, speed-1
            else:
                l = speed+1
        return minSpeed
            

