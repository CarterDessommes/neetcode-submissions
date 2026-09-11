class Twitter:
    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))

        if len(self.posts[userId]) > 10:
            self.posts[userId].pop(0)  # Remove oldest tweet

        self.time -= 1  # Newer tweets have smaller timestamps

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.following[userId].add(userId)

        # Including your own tweets along with those of people you follow
        for followeeId in self.following[userId]:
            # if this person has posts
            if self.posts[followeeId]:
                # most recent is the last one
                index = len(self.posts[followeeId]) - 1
                time, tweetId = self.posts[followeeId][index]

                # Start with each person's newest tweet
                minHeap.append(
                    [time, tweetId, followeeId, index - 1]
                )
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # Add this person's next older tweet
            if index >= 0:
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(
                    minHeap,
                    [time, tweetId, followeeId, index - 1]
                )
        
        heapq.heapify(minHeap)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)