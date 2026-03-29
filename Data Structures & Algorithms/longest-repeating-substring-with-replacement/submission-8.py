class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        best = res = 0
        l = 0
        for r in range(len(s)):
            char[s[r]] = char.get(s[r], 0)+1
            best = max(best, char[s[r]])
            while (r-l)+1 - best > k:
                char[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res