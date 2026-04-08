class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def dfs(i,n,memo):
            if i in memo: return memo[i]
            if i >= n: return 0
            memo[i] = max(nums[i]+dfs(i+2,n,memo),dfs(i+1,n,memo))
            return memo[i]
        return max(dfs(0,n-1,{}),dfs(1,n,{}))