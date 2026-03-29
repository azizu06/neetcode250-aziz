class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        c1 = c2 = 0
        num1 = num2 = -1
        for i in range(len(nums)):
            if num1 == nums[i]:
                c1+=1
            elif num2 == nums[i]:
                c2+=1
            elif c1 == 0:
                num1, c1 = nums[i], 1
            elif c2 == 0:
                num2, c2 = nums[i], 1
            else:
                c1-=1
                c2-=1
        c1 = c2 = 0
        for n in nums:
            if n == num1:
                c1+=1
            elif n == num2:
                c2+=1
        
        if c1 > len(nums)//3:
            res.append(num1)
        if c2 > len(nums)//3:
            res.append(num2)
        return res