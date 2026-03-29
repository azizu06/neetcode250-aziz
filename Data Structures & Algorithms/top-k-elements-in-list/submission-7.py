class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []
        buckets = [[] for _ in range(len(nums)+1)]
        for n in nums:
            freq[n]+=1
        maxCnt = 0
        for key, v in freq.items():
            maxCnt = max(maxCnt, v)
            buckets[v].append(key)
        c = 0
        for i in range(maxCnt, -1, -1):
            for j in range(len(buckets[i])):
                if c == k:
                    break
                res.append(buckets[i][j])
                c+=1
        return res


        
