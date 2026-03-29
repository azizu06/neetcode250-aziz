class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dups = set()
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in dups:
                nums.pop(i)
            else:
                dups.add(nums[i])
                count+=1
        return count