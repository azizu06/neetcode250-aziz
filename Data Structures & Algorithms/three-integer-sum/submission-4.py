class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        nums.sort()
        res = []
        while i < len(nums)-2:
            if i > 0:
                if nums[i] == nums[i-1]:
                    i+=1
                    continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if  total == 0:
                    new = [nums[i], nums[l], nums[r]]
                    res.append(new)
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total > 0:
                    r-=1
                else:
                    l+=1
            i+=1
        return res
            

