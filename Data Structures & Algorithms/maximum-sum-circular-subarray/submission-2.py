class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best = worst = nums[0]
        curMax = curMin = total = 0
        for n in nums:
            curMax = max(n,curMax+n)
            curMin = min(n,curMin+n)
            best = max(best,curMax)
            worst = min(worst,curMin)
            total+=n
        return max(best,total-worst) if best > 0 else best
