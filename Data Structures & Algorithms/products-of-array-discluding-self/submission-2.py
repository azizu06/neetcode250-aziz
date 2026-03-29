class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*(len(nums)+1)
        suf = [1]*(len(nums)+1)
        res = [1]*len(nums)
        for i in range(len(nums)):
            pre[i+1] = pre[i]*nums[i]
        for i in range(len(nums)-1, -1, -1):
            suf[i-1] = suf[i] * nums[i]
        for i in range(len(nums)):
            res[i] = pre[i]*suf[i]
        return res
    