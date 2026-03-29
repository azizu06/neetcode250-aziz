class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0
        et, pt = [], []
        for i, t in enumerate(tasks):
            heapq.heappush(et, (t[0], t[1], i))
        res = []
        while pt or et:
            while et and et[0][0] <= time:
                eTime, pTime, i = heapq.heappop(et)
                heapq.heappush(pt, (pTime, i))
            if not pt:
                time = et[0][0]
                continue
            pTime, i = heapq.heappop(pt)
            time+=pTime
            res.append(i)
        return res