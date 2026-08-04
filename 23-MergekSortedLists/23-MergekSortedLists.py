# Last updated: 04/08/2026 16:02:07
1import heapq
2
3
4# Definition for singly-linked list.
5class ListNode:
6    def __init__(self, val=0, next=None):
7        self.val = val
8        self.next = next
9
10class Solution:
11    def mergeKLists(self, lists):
12        min_heap = []
13        for i, lst in enumerate(lists):
14            if lst:
15                heapq.heappush(min_heap, (lst.val, i, lst))
16                
17        dummy = ListNode()
18        curr = dummy
19        
20        while min_heap:
21            val, i, node = heapq.heappop(min_heap)
22            
23            curr.next = node
24            curr = curr.next
25            
26            if node.next:
27                heapq.heappush(min_heap, (node.next.val, i, node.next))
28                
29        return dummy.next