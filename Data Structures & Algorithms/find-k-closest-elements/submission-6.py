class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        for r, n in enumerate(arr):
            while r-l+1 > k and abs(n-x) < abs(arr[l]-x): l+=1
        return arr[l:l+k]

