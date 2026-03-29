class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        i, j = 0, 0
        while j < len(nums):
            if abs(i-j) > k:
                s.remove(nums[i])
                i+=1
            if nums[j] not in s:
                s.add(nums[j])
            else:
                return True
            j+=1
                
        return False
            
            
