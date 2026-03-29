class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        minWeight = r
        while l <= r:
            cap, total, dayCnt = (l+r)//2, 0, 1
            for w in weights:
                if total + w > cap:
                    total, dayCnt = 0, dayCnt+1
                total+=w
            if dayCnt <= days:
                minWeight, r = cap, cap-1
            else:
                l = cap+1
        return minWeight
                
