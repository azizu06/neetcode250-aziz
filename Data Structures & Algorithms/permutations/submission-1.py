class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]: continue
                path.append(nums[i])
                used[i] = 1
                perm(path, used)
                used[i] = 0
                path.pop()
        perm([], [0]*len(nums))
        return res