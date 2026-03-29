class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        k = 0
        while k < len(nums):
            if k > 0 and nums[k] == nums[k-1]:
                k+=1
                continue
            i, j = k+1, len(nums)-1
            target = -1*nums[k]
            while i < j:
                cur = nums[i] + nums[j]
                if i > k+1 and nums[i] == nums[i-1]:
                    i+=1
                elif cur == target:
                    res.append([nums[i], nums[j], nums[k]])
                    i+=1
                elif cur < target:
                    i+=1
                else:
                    j-=1
            k+=1
        return res
