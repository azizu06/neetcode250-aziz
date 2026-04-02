class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        top = 0
        n = mountainArr.length()
        l, r = 1, n-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            back, front = mountainArr.get(m-1), mountainArr.get(m+1)
            if val > back and val > front:
                top = m
                break
            if val < back:
                r = m-1
            else:
                l = m+1
        res = -1
        l, r = 0, top-1
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target: return m
            if val < target:
                l = m+1
            else:
                r = m-1
        l, r = top,n-1
        while l <= r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val == target: return m
            if val < target:
                r = m-1
            else:
                l = m+1
        return res
            
