# Last updated: 12/08/2026 09:55:49
1import heapq
2
3class KthLargest(object):
4
5    def __init__(self, k, nums):
6        """
7        :type k: int
8        :type nums: List[int]
9        """
10        self.k = k
11        self.min_heap = nums
12        
13        heapq.heapify(self.min_heap)
14        
15        while len(self.min_heap) > self.k:
16            heapq.heappop(self.min_heap)
17
18    def add(self, val):
19        """
20        :type val: int
21        :rtype: int
22        """
23  
24        heapq.heappush(self.min_heap, val)
25    
26        if len(self.min_heap) > self.k:
27            heapq.heappop(self.min_heap)
28            
29      
30        return self.min_heap[0]
31
32
33# Your KthLargest object will be instantiated and called as such:
34# obj = KthLargest(k, nums)
35# param_1 = obj.add(val)