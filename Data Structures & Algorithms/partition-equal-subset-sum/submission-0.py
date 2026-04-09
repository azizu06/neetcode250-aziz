class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2: 
            return False
        target = total//2
        memo = {}
        def dfs(i,target):
            if (i,target) in memo: return memo[(i,target)]
            if not target: return True
            if i == len(nums): return False
            take = False
            if target-nums[i] >= 0:
                take = dfs(i+1,target-nums[i])
            skip = dfs(i+1,target)
            memo[(i,target)] = take or skip
            return memo[(i,target)]
        return dfs(0,target)

            