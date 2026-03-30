class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def rec(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue
                path.append(nums[i])
                used[i] = 1
                rec(path, used)
                used[i] = 0
                path.pop()
        rec([], [0]*len(nums))
        return res
