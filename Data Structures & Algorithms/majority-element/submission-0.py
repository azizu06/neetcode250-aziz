class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        myMap = {}
        target = len(nums)/2
        for n in nums:
            myMap[n] = myMap.get(n, 0) + 1
        for k, v in myMap.items():
            if v > target:
                return k
    