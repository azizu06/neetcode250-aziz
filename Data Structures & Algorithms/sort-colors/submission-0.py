class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 1
        while i < len(nums):
            val = nums[i]
            j = i-1
            while j >= 0 and nums[j] > val:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = val
            i+=1
