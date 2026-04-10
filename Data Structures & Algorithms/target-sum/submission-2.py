class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,cur):
            if (i,cur) in memo: return memo[(i,cur)]
            if i == len(nums): return 1 if cur == target else 0
            memo[(i,cur)] = dfs(i+1,cur-nums[i])+dfs(i+1,cur+nums[i])
            return memo[(i,cur)]
        return dfs(0,0)