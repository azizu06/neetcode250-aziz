class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            freq[fruits[r]]+=1
            while len(freq) > 2:
                freq[fruits[l]]-=1
                if not freq[fruits[l]]:
                    del freq[fruits[l]]
                l+=1
            res = max(res, r-l+1)
        return res

