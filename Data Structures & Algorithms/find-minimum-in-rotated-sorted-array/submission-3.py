class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        sm = 1001
        while l <= r:
            m = (l+r)//2
            if nums[l] <= nums[m]:
                sm = min(sm, nums[l])
                l = m+1
            else:
                sm = min(sm, nums[m])
                r = m-1
        return sm