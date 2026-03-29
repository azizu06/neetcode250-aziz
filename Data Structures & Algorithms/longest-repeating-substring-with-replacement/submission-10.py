class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = res = best = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0)+1
            best = max(best, freq[s[r]])
            if r-l+1-best<=k:
                res = max(res, r-l+1)
            else:
                freq[s[l]]-=1
                l+=1
        return res
