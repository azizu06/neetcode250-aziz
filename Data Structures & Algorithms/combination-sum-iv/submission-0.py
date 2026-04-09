class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target):
            if not dp[i]: continue
            for n in nums:
                if i+n > target: continue
                dp[i+n]+=dp[i]
        return dp[-1]
