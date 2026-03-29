class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        dq = deque()
        time = 0
        heapq.heapify(heap)
        while heap or dq:
            time+=1
            if heap: 
                cnt = 1+heapq.heappop(heap)
                if cnt: dq.append([cnt, time+n])
            if dq and dq[0][1] == time:
                heapq.heappush(heap, dq.popleft()[0])
        return time






        
        