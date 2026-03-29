class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        res =  [[] for i in range(len(nums)+1)]
        res2 = []
        for n in nums:
            myMap[n] = myMap.get(n, 0) + 1
        for key in myMap:
            res[myMap[key]].append(key)
        maxValue = max(myMap.values())
        for i in range(maxValue, -1, -1):
            for j in range(len(res[i])):
                res2.append(res[i][j])
                if len(res2) == k:
                    return res2