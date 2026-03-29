class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, m, res = 0, {}, 0
        for r in range(len(s)):
            if s[r] in m:
                l = max(l, m[s[r]]+1)
            res = max(res, r-l+1)
            m[s[r]] = r
        return res