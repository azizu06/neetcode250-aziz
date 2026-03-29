class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, diff = 0, float('inf')
        for r, n in enumerate(arr):
            while r-l+1 > k:
                if abs(n-x) >= abs(arr[l]-x): break
                l+=1
        res = [0]*k
        for i in range(k):
            res[i] = arr[l]
            l+=1
        return res

