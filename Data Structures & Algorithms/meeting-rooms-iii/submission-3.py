class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = {i: 0 for i in range(n)}
        meetings.sort()
        avail = [i for i in range(n)]
        heapq.heapify(avail)
        meet = []
        for start, end in meetings:
            while meet and start >= meet[0][0]:
                heapq.heappush(avail,(heapq.heappop(meet)[1]))
            if avail:
                curRoom = heapq.heappop(avail)
                heapq.heappush(meet,(end,curRoom))
            else:
                newStart, curRoom = heapq.heappop(meet)
                newEnd = end+(newStart-start)
                heapq.heappush(meet,(newEnd,curRoom))
            rooms[curRoom]+=1
            
        res = best = 0
        for room,numMeetings in rooms.items():
            if numMeetings > best:
                res = room
                best = numMeetings
        return res

                


