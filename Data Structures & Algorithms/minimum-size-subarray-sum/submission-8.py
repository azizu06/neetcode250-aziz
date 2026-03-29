class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre, res = [0]*(len(nums)+1), len(nums)+1
        for i in range(len(nums)):
            pre[i+1] = pre[i]+nums[i]
        for i in range(1, len(pre)):
            l, r = i, len(pre)-1
            while l<=r:
                m = (l+r)//2
                if pre[m]-pre[i-1] >= target:
                    res = min(res, m-i+1)
                    r = m-1
                else:
                    l = m+1
        return 0 if res == len(nums)+1 else res

            

