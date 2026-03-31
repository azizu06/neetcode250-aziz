class MedianFinder:

    def __init__(self):
        self.maxH = []
        self.minH = []

    def addNum(self, num: int) -> None:
        if self.maxH and num < -self.maxH[0]:
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
            return self.minH[0]
        elif maxLen > minLen:
            return -self.maxH[0]
        else:
            return (-self.maxH[0]+self.minH[0])/2.0

        
        