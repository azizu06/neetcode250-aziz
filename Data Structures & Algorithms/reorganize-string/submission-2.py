class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)
        maxFreq = 0
        for c in s:
            freq[c] = freq.get(c, 0)+1
            maxFreq = max(freq[c], maxFreq)
        if maxFreq > math.ceil(len(s)/2): return ""
        res = []
        wait, heap = deque(), []
        for char, cnt in freq.items():
            heapq.heappush(heap, (-cnt, char))
        while heap or wait:
            if wait and wait[0][1] != res[-1]: 
                cnt, char = wait.popleft()
                heapq.heappush(heap, (cnt, char))
            cnt, char = heapq.heappop(heap)
            res.append(char)
            cnt+=1
            if cnt: wait.append([cnt, char])
        return "".join(res)


