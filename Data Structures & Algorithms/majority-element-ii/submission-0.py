class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        counts = {}
        valid  = len(nums)//3
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for key in counts:
            if counts[key] > valid:
                res.append(key)
        return res