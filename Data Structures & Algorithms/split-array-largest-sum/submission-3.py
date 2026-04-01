class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def groups(target):
            total, sub = 0, 1
            for n in nums:
                if total+n > target:
                    total, sub = 0, sub+1
                    if sub > k: return sub
                total+=n
            return sub
        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            m = (l+r)//2
            cnt = groups(m)
            if cnt <= k:
                res = m
                r = m-1
            else:
                l = m+1
        return res