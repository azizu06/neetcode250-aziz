class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in self.map:
                return [self.map[diff], i]
            self.map[nums[i]] = i


