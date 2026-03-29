class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minWeight = sum(weights)
        l, r = max(weights), minWeight
        while l <= r:
            cap = (l+r)//2
            total = dayCnt = 0
            for w in weights:
                if total + w > cap:
                    total = 0
                    dayCnt+=1
                total+=w
            dayCnt+=1
            if dayCnt <= days:
                minWeight = cap
                r = cap-1
            else:
                l = cap+1
        return minWeight
                
