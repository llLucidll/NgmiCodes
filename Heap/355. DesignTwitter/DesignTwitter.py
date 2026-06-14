import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.following = {} # user Id -> set(following)
        self.tweets = {} # user Id -> arr[tweets]

    def ensureUser(self, userId) -> None:
        if userId not in self.following:
            self.following[userId] = set()
            self.following[userId].add(userId)
            
            self.tweets[userId] = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.ensureUser(userId)

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    
    def getNewsFeed(self, userId: int) -> list[int]:
        self.ensureUser(userId)
        feed = []
        heap = []
        
        for followeeId in self.following[userId]:
            if self.tweets[followeeId]:
                heap.append((
                    -self.tweets[followeeId][-1][0], 
                    self.tweets[followeeId][-1][1], 
                    -1, 
                    followeeId
                ))
        
        heapq.heapify(heap)
        while len(feed) < 10 and heap:
            _, tweet, index, followeeId = heapq.heappop(heap)
            index -= 1
            feed.append(tweet)
            if len(self.tweets[followeeId]) >= index * -1:
                next_tweet = self.tweets[followeeId][index]
                heapq.heappush(heap, (-next_tweet[0], next_tweet[1], index, followeeId))
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensureUser(followerId)
        self.ensureUser(followeeId)

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        self.ensureUser(followerId)
        self.ensureUser(followeeId)

        if followeeId not in self.following[followerId]:
            return

        self.following[followerId].remove(followeeId)

        

