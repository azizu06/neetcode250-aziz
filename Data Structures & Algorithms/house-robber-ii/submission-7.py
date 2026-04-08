class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for i,n in enumerate(nums):
            if not i: continue
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
        res = rob2
        rob1, rob2 = 0,0
        for i,n in enumerate(nums):
            if i == len(nums)-1: continue
            temp = max(rob1+n,rob2)
            rob1 = rob2
            rob2 = temp
        return max(nums[0],res,rob2)

