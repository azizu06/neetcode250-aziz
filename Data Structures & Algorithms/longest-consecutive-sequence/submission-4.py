class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0
        for n in seq:
            if n-1 in seq:
                continue
            cur = 1
            while n+cur in seq:
                cur+=1
            longest = max(cur, longest)
        return longest
            
