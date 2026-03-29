class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets: self.tweets[userId] = []
        if userId not in self.follows: self.follows[userId] = {}
        self.follows[userId][userId] = True
        self.tweets[userId].append([self.time, tweetId])
        self.time+=1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        for followee, following in self.follows[userId].items():
            if following and followee in self.tweets:
                tweet = self.tweets[followee][-1]
                heapq.heappush(heap, (-tweet[0], tweet[1], followee, len(self.tweets[followee])-1))
        while len(res) < 10 and heap:
            _, tweet, user, i = heapq.heappop(heap)
            res.append(tweet)
            if i-1 >= 0:
                tweet = self.tweets[user][i-1]
                heapq.heappush(heap, (-tweet[0], tweet[1], user, i-1))
        return res
            
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        if followerId not in self.follows: self.follows[followerId] = {}
        self.follows[followerId][followeeId] = True
        self.follows[followerId][followerId] = True
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.follows[followerId][followeeId] = False
        
