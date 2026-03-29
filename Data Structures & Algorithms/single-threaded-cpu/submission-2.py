class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        et, pt = [], []
        for i, t in enumerate(tasks):
            heapq.heappush(et, (t[0], t[1], i))
        eTime, pTime, i = heapq.heappop(et)
        heapq.heappush(pt, (pTime, i, eTime))
        res = []
        while pt:
            pTime, i, eTime = heapq.heappop(pt)
            if time < eTime: time = eTime
            time+=pTime
            res.append(i)
            while et and et[0][0] <= time:
                eTime, pTime, i = heapq.heappop(et)
                heapq.heappush(pt, (pTime, i, eTime))
            if et and not pt:
                eTime, pTime, i = heapq.heappop(et)
                heapq.heappush(pt, (pTime, i, eTime))
        return res