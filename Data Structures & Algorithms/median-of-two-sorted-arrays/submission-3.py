class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x,y = nums1, nums2
        if len(y) < len(x):
            x,y = y,x
        total = len(x)+len(y)
        half = total//2
        l, r = 0, len(x)-1
        while True:
            px = (l+r)//2
            py = half-px-2
            xLeft = x[px] if px >= 0 else float('-inf')
            xRight = x[px+1] if px+1 < len(x) else float('inf')
            yLeft = y[py] if py >= 0 else float('-inf')
            yRight = y[py+1] if py+1 < len(y) else float('inf')

            if xLeft <= yRight and yLeft <= xRight:
                if total % 2 == 1:
                    return min(xRight, yRight)
                return (max(xLeft,yLeft)+min(xRight, yRight))/2
            elif xLeft > yRight:
                r = px-1
            else:
                l = px+1

