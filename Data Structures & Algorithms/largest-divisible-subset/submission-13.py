class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        res = []
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j]%nums[i]: continue
                tmp = [nums[i]]+dp[j]
                dp[i] = tmp if len(tmp) > len(dp[i]) else dp[i]
            res = dp[i] if len(dp[i]) > len(res) else res
        return res
                

            