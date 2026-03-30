class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(candidates)
        def rec(start, path, total):
            if total == target: res.append(path[:])
            for i in range(start, len(nums)):
                if total+nums[i] > target: return
                if i > start and nums[i] == nums[i-1]: continue
                path.append(nums[i])
                rec(i+1, path, total+nums[i])
                path.pop()
        rec(0, [], 0)
        return res
