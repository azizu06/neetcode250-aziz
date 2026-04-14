class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = farthest = 0
        n = len(nums)
        if n == 1: return 0
        while r < n-1:
            for i in range(l,r+1):
                farthest = max(farthest,nums[i]+i)
            l = r+1
            r = farthest
            res+=1
        return res
            
