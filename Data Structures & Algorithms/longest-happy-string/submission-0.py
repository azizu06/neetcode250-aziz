class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = [[-a, "a"], [-b, "b"], [-c, "c"]]
        heapq.heapify(heap)
        wait = None
        while heap or wait:
            if not heap: break
            cnt, char = heapq.heappop(heap)
            if not cnt: continue
            res.append(char)
            cnt+=1
            if wait:
                heapq.heappush(heap, wait)
                wait = None
            if cnt:
                if len(res) >= 2 and res[-1] == res[-2] == char:
                    wait = [cnt, char]
                else:
                    heapq.heappush(heap, [cnt, char])
        return "".join(res)
        #ccbcc