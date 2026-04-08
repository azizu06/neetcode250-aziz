class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        small = res = best = nums[0]
        for n in nums[1:]:
            tmp = best*n
            best = max(n,tmp,small*n)
            small = min(n,tmp,small*n)
            res = max(res,best)
        return res
