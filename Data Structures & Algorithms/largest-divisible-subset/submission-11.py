class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dfs(i):
            if i == len(nums): return []
            if i in memo: return memo[i]
            longest = [nums[i]]
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]: continue
                path = [nums[i]]+dfs(j)
                if len(path) > len(longest):
                    longest = path
            memo[i] = longest
            return longest
        return dfs(0)
            