class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if slow == fast: return slow
