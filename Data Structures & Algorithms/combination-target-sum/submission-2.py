class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def rec(start, path, total):
            if total == target: res.append(path[:])
            for i in range(start, len(nums)):
                if total+nums[i] > target: return
                path.append(nums[i])
                rec(i, path, total+nums[i]) 
                path.pop()
        rec(0, [], 0)
        return res
        