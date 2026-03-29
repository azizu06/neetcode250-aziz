class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(start, path):
            total = sum(path)
            if total == target: res.append(path[:])
            for i in range(start, len(nums)):
                if total+nums[i] > target: continue
                path.append(nums[i])
                rec(i, path) 
                path.pop()
        rec(0, [])
        return res
        