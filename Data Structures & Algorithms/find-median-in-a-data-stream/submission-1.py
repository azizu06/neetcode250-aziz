class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []

    def addNum(self, num: int) -> None:
        if not self.maxH and not self.minH:
            heapq.heappush(self.minH, num)
        elif self.minH and not self.maxH:
            if num > self.minH[0]:
                heapq.heappush(self.minH, num)
            else:
                heapq.heappush(self.maxH, -num)
        elif self.maxH and not self.minH:
            if num < -self.maxH[0]:
                heapq.heappush(self.maxH, -num)
            else:
                heapq.heappush(self.minH, num)
        elif num < -self.maxH[0]:
            heapq.heappush(self.maxH, -num)
        else:
            heapq.heappush(self.minH, num)

        minLen, maxLen = len(self.minH), len(self.maxH)
        if minLen-maxLen >= 2:
            heapq.heappush(self.maxH, -heapq.heappop(self.minH))
        elif maxLen-minLen >= 2:
            heapq.heappush(self.minH, -(heapq.heappop(self.maxH)))
        
    def findMedian(self) -> float:
        minLen, maxLen = len(self.minH), len(self.maxH)
        if minLen > maxLen:
            return self.minH[0]/1.0
        elif maxLen > minLen:
            return -self.maxH[0]/1.0
        else:
            return (self.minH[0]+(-self.maxH[0]))/2.0

        
        