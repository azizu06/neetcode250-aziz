class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        top = 0
        n = mountainArr.length()
        cache = {}
        def get(i):
            if i not in cache: cache[i] = mountainArr.get(i)
            return cache[i]
        l, r = 1, n-2
        while l<=r:
            m = (l+r)//2
            left, mid, right = get(m-1), get(m), get(m+1)
            if mid > left and mid > right:
                top = m
                break
            if mid < left:
                r = m-1
            else:
                l = m+1
        l, r = 0, top-1
        while l <= r:
            m = (l+r)//2
            val = get(m)
            if val == target: return m
            if val < target:
                l = m+1
            else:
                r = m-1
        l, r = top,n-1
        while l <= r:
            m = (l+r)//2
            val = get(m)
            if val == target: return m
            if val < target:
                r = m-1
            else:
                l = m+1
        return -1
            
