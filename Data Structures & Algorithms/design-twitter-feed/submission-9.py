class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time-=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee in self.tweets:
                tweet = self.tweets[followee][-1]
                heapq.heappush(heap, (tweet[0], tweet[1], followee, len(self.tweets[followee])-1))
        while len(res) < 10 and heap:
            _, tweet, user, i = heapq.heappop(heap)
            res.append(tweet)
            if i-1 >= 0:
                tweet = self.tweets[user][i-1]
                heapq.heappush(heap, (tweet[0], tweet[1], user, i-1))
        return res
            
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        self.follows[followerId].add(followerId)

    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: self.follows[followerId].remove(followeeId)
        
