# Last updated: 12/08/2026 11:47:18
1from collections import Counter, deque
2import heapq
3
4class Solution(object):
5    def leastInterval(self, tasks, n):
6        """
7        :type tasks: List[str]
8        :type n: int
9        :rtype: int
10        """
11        count = Counter(tasks) 
12        
13        tas = [-c for c in count.values()]
14        heapq.heapify(tas)
15
16        file_attente = deque()
17        t = 0
18
19        while tas or file_attente:
20            t += 1
21            
22            if tas:
23                
24                c = heapq.heappop(tas) + 1
25                
26                if c != 0:
27                    file_attente.append([c, t + n])
28            
29            if file_attente and file_attente[0][1] == t:
30                tache_repose = file_attente.popleft()
31
32                heapq.heappush(tas, tache_repose[0])
33                
34        return t