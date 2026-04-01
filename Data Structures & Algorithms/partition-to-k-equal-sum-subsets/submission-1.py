class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k: return False
        target = total//k
        sets = [0]*k
        nums.sort(reverse=True)
        def dfs(i):
            if i == len(nums): return True
            for j in range(k):
                if sets[j]+nums[i] > target: continue
                sets[j]+=nums[i]
                if dfs(i+1): return True
                sets[j]-=nums[i]
                if sets[j] == 0: break
            return False
        return dfs(0)
            