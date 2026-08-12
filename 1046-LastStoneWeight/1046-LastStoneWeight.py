# Last updated: 12/08/2026 10:12:23
1import heapq
2
3class Solution(object):
4    def lastStoneWeight(self, stones):
5        """
6        :type stones: List[int]
7        :rtype: int
8        """
9
10        valeurs_inversees = [-x for x in stones]
11        heapq.heapify(valeurs_inversees)
12        while len(valeurs_inversees) >=2:
13            y = heapq.heappop(valeurs_inversees)
14            x = heapq.heappop(valeurs_inversees)
15            if x != y:
16                heapq.heappush(valeurs_inversees,y - x)
17
18        if len(valeurs_inversees) ==0 :
19            return 0 
20        
21
22        return -valeurs_inversees[0]
23
24   
25       