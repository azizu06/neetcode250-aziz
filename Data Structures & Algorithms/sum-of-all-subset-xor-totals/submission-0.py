class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def rec(start, path):
            nonlocal res
            total = 0
            for n in path:
                total^=n
            res+=total
            for i in range(start, len(nums)):
                path.append(nums[i])
                rec(i+1, path)
                path.pop()
        rec(0, [])
        return res