class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = [1]
        suffix = [1]
        i = 0
        val = 1
        while i < len(nums):
            val *= nums[i]
            prefix.append(val)
            i += 1
        j = len(nums)-1
        val2 = 1
        while j > 0:
            val2 *= nums[j]
            suffix.insert(0,val2)
            j -= 1
        k = 0
        while k < len(nums):
            res[k] = prefix[k] * suffix[k]
            k += 1 
        return res




