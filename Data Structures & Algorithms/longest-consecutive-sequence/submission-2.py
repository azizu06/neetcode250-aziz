class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for n in nums:
            mySet.add(n)
        max = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in mySet:
                continue
            j = 0
            count = 0
            while (nums[i]+j) in mySet:
                count += 1
                j += 1
            if(count > max):
                max = count
        return max
            
