class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res=[]
        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r-=1
            elif twoSum < target:
                l+=1
            else:
                res.extend([l+1,r+1])
                break
        return res