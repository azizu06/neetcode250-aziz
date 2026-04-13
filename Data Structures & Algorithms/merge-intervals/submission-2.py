class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]
        for start,end in intervals[1:]:
            if start <= prev[1]:
                prev[1] = max(prev[1],end)
            else:
                res.append(prev)
                prev = [start,end]
        return res+[prev]
            
            

