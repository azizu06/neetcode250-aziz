class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for n in nums:
            new = defaultdict(int)
            for total,cnt in dp.items():
                new[total+n]+=cnt
                new[total-n]+=cnt
            dp = new
        return dp[target]