class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1]-x[0])
        res = [-1]*len(queries)
        for i,t in enumerate(queries):
            found = False
            for start,end in intervals:
                if start <= t <= end:
                    if not found:
                        res[i] = end-start+1
                        found = True
            if not found: res[i] = -1
        return res
                