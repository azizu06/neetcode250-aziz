class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cur = set()
        freq = Counter(s)
        l = 0
        res = []
        for r in range(len(s)):
            freq[s[r]]-=1
            cur.add(s[r])
            if not freq[s[r]]:
                cur.remove(s[r])
            if not cur:
                res.append(r-l+1)
                l = r+1
        return res

    