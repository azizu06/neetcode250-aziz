class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 1
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0][1]
        for start,end in intervals[1:]:
            if start >= prev:
                res+=1
                prev = end
            prev = min(prev,end)
        return len(intervals)-res

"""
[1,100][1,11],[2,12],[11,22]
[1,11],[2,12],[11,22],[1,100]
[1,2],[2,4],[1,4]
"""