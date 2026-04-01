class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def groups(target):
            total, k = 0, 1
            for n in nums:
                if total+n > target:
                    total, k = 0, k+1
                total+=n
            return k
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