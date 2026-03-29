class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res not in myMap:
                myMap[nums[i]] = i
            else:
                return [myMap[res], i] 