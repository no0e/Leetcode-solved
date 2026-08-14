# Last updated: 14/08/2026 15:34:40
1class Twitter(object):
2
3    def __init__(self):
4        self.timestamp = 0 
5        self.tweets = collections.defaultdict(list)
6        self.following = collections.defaultdict(set)
7
8    def postTweet(self, userId, tweetId):
9        """
10        :type userId: int
11        :type tweetId: int
12        :rtype: None
13        """
14        self.tweets[userId].append((self.timestamp, tweetId))
15        self.timestamp -= 1 
16
17    def getNewsFeed(self, userId):
18        """
19        :type userId: int
20        :rtype: List[int]
21        """
22        minHeap = []
23        
24        users = self.following[userId] | {userId}
25
26        for u in users:
27            if self.tweets[u]:
28                index = len(self.tweets[u]) - 1
29                time, tweetId = self.tweets[u][index]
30                # Store: (timestamp, tweetId, userId, index_in_user_tweet_list)
31                minHeap.append((time, tweetId, u, index))
32        heapq.heapify(minHeap)
33        
34        res = []
35
36        while minHeap and len(res) < 10:
37            time, tweetId, u, index = heapq.heappop(minHeap)
38            res.append(tweetId)
39        
40            if index > 0:
41                next_index = index - 1
42                next_time, next_tweetId = self.tweets[u][next_index]
43                heapq.heappush(minHeap, (next_time, next_tweetId, u, next_index))
44                
45        return res
46
47    def follow(self, followerId, followeeId):
48        """
49        :type followerId: int
50        :type followeeId: int
51        :rtype: None
52        """
53        self.following[followerId].add(followeeId)
54
55    def unfollow(self, followerId, followeeId):
56        """
57        :type followerId: int
58        :type followeeId: int
59        :rtype: None
60        """
61        if followeeId in self.following[followerId]:
62            self.following[followerId].remove(followeeId)
63        
64
65
66# Your Twitter object will be instantiated and called as such:
67# obj = Twitter()
68# obj.postTweet(userId,tweetId)
69# param_2 = obj.getNewsFeed(userId)
70# obj.follow(followerId,followeeId)
71# obj.unfollow(followerId,followeeId)