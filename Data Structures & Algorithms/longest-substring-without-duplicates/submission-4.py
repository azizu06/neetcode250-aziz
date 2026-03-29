class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = {}
        l = res = 0
        for r in range(len(s)):
            if s[r] in dup:
                l = max(l, dup[s[r]]+1)
            dup[s[r]] = r
            res = max(res, r-l+1)
        return res