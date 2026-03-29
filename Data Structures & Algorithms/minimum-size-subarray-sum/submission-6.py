class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre = [0]*len(nums)
        pre[0], res = nums[0], len(pre)+1
        if pre[0] >= target: res = 1
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]+nums[i]
            if pre[i] >= target:
                res = min(res, i+1)
        for i in range(len(pre)):
            l, r = i, len(nums)-1
            while l<=r:
                m = (l+r)//2
                if pre[m]-pre[i] >= target:
                    res = min(res, m-i)
                    r = m-1
                else:
                    l = m+1
        return 0 if res == len(pre)+1 else res

            

