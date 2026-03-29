class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums)-3:
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i+1
            while j < len(nums)-2:
                if nums[j] == nums[j-1] and j > i+1:
                    j+=1
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    if nums[k] == nums[k-1] and k > j+1:
                        k+=1
                        continue
                    if l < len(nums)-1 and nums[l] == nums[l+1]:
                        l-=1
                        continue
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                    if nums[i]+nums[j]+nums[k]+nums[l] > target:
                        l -= 1
                    if nums[i]+nums[j]+nums[k]+nums[l] < target:
                        k += 1
                j+=1
            i+=1
        
        return res


#  i j k     l
# -3,0,1,2,3,3
#        i j k l
# -1,-1,-1,1,1,1