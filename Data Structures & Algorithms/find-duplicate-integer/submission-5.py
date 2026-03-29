class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        j, n = 1, len(nums)
        for i in range(n):
            for _ in range(2):
                j%=n
                if i != j and nums[(j+1)%n] == nums[i] or nums[j] == nums[i]:
                    return nums[i]
                elif nums[j] == nums[(j+1)%n]:
                    return nums[j]
                j+=1
