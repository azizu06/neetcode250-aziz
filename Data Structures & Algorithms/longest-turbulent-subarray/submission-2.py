class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,res = 0,1
        sign = ""
        for r in range(len(arr)-1):
            if arr[r] == arr[r+1]:
                res = max(res,r-l+1)
                l = r+1
                sign = ""
                continue
            if sign == "<" and arr[r] < arr[r+1] or (sign == ">" and arr[r] > arr[r+1]):
                l = r
            else:
                res = max(res,r-l+2)
            sign = "<" if arr[r] < arr[r+1] else ">"
        return res
            