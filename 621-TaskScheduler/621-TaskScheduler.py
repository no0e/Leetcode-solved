# Last updated: 12/08/2026 11:46:56
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
13        # 1. On crée d'abord la liste classique
14        tas = [-c for c in count.values()]
15        # 2. On la transforme en tas sur place (ne rien assigner à une variable)
16        heapq.heapify(tas)
17
18        file_attente = deque()
19        t = 0
20
21        while tas or file_attente:
22            t += 1
23            
24            if tas:
25                # 3. On utilise bien la variable 'tas' ici
26                c = heapq.heappop(tas) + 1
27                
28                if c != 0:
29                    file_attente.append([c, t + n])
30            
31            if file_attente and file_attente[0][1] == t:
32                tache_repose = file_attente.popleft()
33                # 3. On utilise bien la variable 'tas' ici aussi
34                heapq.heappush(tas, tache_repose[0])
35                
36        return t