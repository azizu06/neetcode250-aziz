class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [0]*(len(nums1)+len(nums2))
        i = j = k = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i,k = i+1, k+1
            else:
                res[k] = nums2[j]
                j,k = j+1, k+1
        while i<len(nums1):
            res[k] = nums1[i]
            i,k = i+1, k+1
        while j<len(nums2):
            res[k] = nums2[j]
            j,k = j+1, k+1
        n = len(res)
        if n % 2 == 0:
            return (res[(n-1)//2]+res[(n-1)//2+1])/2
        return res[n//2]

