class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        l = r = 0
        res = 0
        while r < len(s):
            if s[r] not in dup:
                dup[s[r]] = r
            else:
                l = max(l, dup[s[r]]+1)
                dup[s[r]] = r
            r+=1
            res = max(res, r-l)
        return res