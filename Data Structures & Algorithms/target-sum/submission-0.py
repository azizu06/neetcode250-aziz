class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,cur):
            if (i,cur) in memo: return memo[(i,cur)]
            if i == len(nums) and cur == target: return 1
            if i == len(nums): return 0
            res = 0
            res+=dfs(i+1,cur-nums[i])+dfs(i+1,cur+nums[i])
            memo[(i,cur)] = res
            return res
        return dfs(0,0)