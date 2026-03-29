class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid-1
            else:
                res = mid
                l = mid+1
        return res