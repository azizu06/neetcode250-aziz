class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [[-cnt, char] for char, cnt in freq.items()]
        res = []
        wait = None
        heapq.heapify(heap)
        while heap or wait:
            if not heap: return ""
            cnt, char = heapq.heappop(heap)
            res.append(char)
            cnt+=1
            if wait: 
                heapq.heappush(heap, wait)
                wait = None
            if cnt: wait = [cnt, char]
        return "".join(res)


