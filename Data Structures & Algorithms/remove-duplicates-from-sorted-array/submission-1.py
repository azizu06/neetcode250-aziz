class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = len(nums)-1, len(nums)-2
        count = 1
        while j >= 0:
            if nums[i] == nums[j]:
                nums.pop(i)
            else:
                count+=1
            i-=1
            j-=1
        return count