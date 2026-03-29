class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r, minWeight = max(weights), sum(weights), sum(weights)
        while l <= r:
            cap, total, dayCnt = (l+r)//2, 0, 0
            for w in weights:
                if total + w > cap:
                    total, dayCnt = 0, dayCnt+1
                total+=w
            dayCnt+=1
            if dayCnt <= days:
                minWeight, r = cap, cap-1
            else:
                l = cap+1
        return minWeight
                
