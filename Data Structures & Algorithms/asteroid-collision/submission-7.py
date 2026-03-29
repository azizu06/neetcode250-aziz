class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if not res:
                res.append(a)
            elif res[-1] > 0 and a < 0:
                while res and abs(a) > abs(res[-1]) and res[-1] > 0:
                    res.pop()
                if not res or res[-1] < 0:
                    res.append(a)
                elif res[-1] > 0 and a < 0 and abs(a) == abs(res[-1]):
                    res.pop()
                elif abs(a) == abs(res[-1]):
                    res.append(a)
            else:
                res.append(a)
        return res