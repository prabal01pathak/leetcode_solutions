from collections import defaultdict, deque
import heapq

class Twitter:
    def __init__(self):
        self.user = defaultdict(set)
        self.posts = []
        heapq.heapify(self.posts)
        
    def check_register(self, userId):
        if userId not in self.user:
            self.user[userId] = set()
            self.user[userId].add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.check_register(userId)
        if len(self.posts) == 0:
            data = [-1, userId, tweetId]
        else:
            prev_pri = self.posts[0][0]
            data = [prev_pri-1, userId, tweetId]
        heapq.heappush(self.posts, data)
        
    def check_follow(self, userId, followeeId):
        user = self.user.get(userId, set())
        if followeeId in user:
            return True
        return False

    def getNewsFeed(self, userId: int) -> List[int]:
        self.check_register(userId)
        res = deque()
        push_again = []
        k = 0
        print(self.posts)
        while k < 10 and len(self.posts) > 0:
            data = heapq.heappop(self.posts)
            if self.check_follow(userId, data[1]):
                res.append(data[2])
                k += 1
            push_again.append(data)
        for i in push_again:
            heapq.heappush(self.posts, i)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.check_register(followerId)
        self.user[followerId].add(followeeId)
        print("FolloweeId: ", followeeId)
        print("Follow: ", self.user)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.check_register(followerId)
        try:
            self.user[followerId].remove(followeeId)
        except Exception as _e:
            pass
        print("FolloweeId: ", followeeId)
        print("unfollow: ", self.user)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)