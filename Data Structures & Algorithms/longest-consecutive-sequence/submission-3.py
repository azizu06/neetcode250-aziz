class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        longest = 0
        for n in nums:
            if n in seq:
                continue
            long = 1
            temp = n-1
            while temp in seq:
                temp, long = temp-1, long+1
            temp = n+1
            while temp in seq:
                temp, long = temp+1, long+1
            longest = max(long, longest)
            seq.add(n)
        return longest
            
