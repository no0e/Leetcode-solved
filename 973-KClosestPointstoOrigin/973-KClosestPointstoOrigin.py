# Last updated: 12/08/2026 10:41:39
1import heapq
2
3class Solution(object):
4    def kClosest(self, points, k):
5        """
6        :type points: List[List[int]]
7        :type k: int
8        :rtype: List[List[int]]
9        """
10        heap = []
11        
12        for x, y in points:
13            
14            dist = x**2 + y**2
15            
16            if len(heap) < k:
17                heapq.heappush(heap, (-dist, x, y))
18            else:
19                heapq.heappushpop(heap, (-dist, x, y))
20                
21        return [[x, y] for dist, x, y in heap]