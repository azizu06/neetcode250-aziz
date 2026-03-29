class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        l, r = 0, len(self.times[key])-1
        res = ""
        while l<=r:
            mid = (l+r)//2
            if self.times[key][mid][0] <= timestamp:
                res = self.times[key][mid][1]
                l = mid+1
            else:
                r = mid-1
        return res

        
