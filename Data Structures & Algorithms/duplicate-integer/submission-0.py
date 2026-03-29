class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i, n in enumerate(nums):
            if n in mySet:
                return True
            mySet.add(n)
        return False

        
