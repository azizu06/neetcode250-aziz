class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bin(nums, l, r, target):
            if l > r:
                return r+1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bin(nums, mid+1, r, target)
            else:
                return bin(nums, l, mid-1, target)
        res = bin(nums, 0, len(nums)-1, target)
        return res