class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def rec(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: continue
                path.append(nums[i])
                rec(i+1, path)
                path.pop()
        rec(0, [])
        return res
                