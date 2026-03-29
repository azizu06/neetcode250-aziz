class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, res, total = 0, len(nums)+1, 0
        for r in range(len(nums)):
            total+=nums[r]
            if total >= target:
                res = min(res, r-l+1)
                while total >= target:
                    total -= nums[l]
                    l+=1
                    if total >= target:
                        res = min(res, r-l+1)
        return 0 if res == len(nums)+1 else res
