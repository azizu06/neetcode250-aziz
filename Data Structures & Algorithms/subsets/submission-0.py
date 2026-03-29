class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                rec(i+1, path)
                path.pop()
        rec(0, [])
        return res