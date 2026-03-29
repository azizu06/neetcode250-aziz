class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        res =  []
        for n in nums:
            myMap[n] = myMap.get(n, 0) + 1
        items = sorted(myMap, key=lambda k: myMap[k], reverse=True)
        for i in range(k):
            res.append(items[i])
        return res