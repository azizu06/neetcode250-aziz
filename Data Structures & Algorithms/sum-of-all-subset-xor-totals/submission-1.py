class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def rec(i, total):
            if i == len(nums):
                return total
            return rec(i+1, total) + rec(i+1, total^nums[i])
        return rec(0, 0)