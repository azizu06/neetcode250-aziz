class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        res1 = float('inf')
        res = 0
        while l<=r:
            m = (l+r)//2
            if abs(arr[m]-x) < res1:
                res = m
                res1 = abs(arr[m]-x)
            if arr[m] <= x:
                l = m+1
            else:
                r = m-1
        l = r = res
        while r-l+1 < k:
            if l == 0:
                r+=1
            elif r == len(arr)-1:
                l-=1
            elif abs(arr[r+1]-x) < abs(arr[l-1]-x):
                r+=1
            else:
                l-=1
        return arr[l:r+1]


