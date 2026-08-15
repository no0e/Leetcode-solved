# Last updated: 15/08/2026 15:10:31
1import heapq
2class MedianFinder(object):
3
4    def __init__(self):
5        self.tas_gauche = []
6        self.tas_droite = []
7        self.longeur_paire = True
8        self.mediane = None
9
10    def addNum(self, num):
11        """
12        :type num: int
13        :rtype: None
14        """
15        if self.mediane is None: 
16            self.mediane = float(num)
17            self.longeur_paire = False
18        else: 
19            if num > self.mediane:
20                heapq.heappush(self.tas_droite, num)
21                
22                if self.longeur_paire:
23                    self.mediane = float(heapq.heappop(self.tas_droite))
24                else: 
25                    heapq.heappush(self.tas_gauche, -self.mediane)
26                    self.mediane = (-self.tas_gauche[0] + self.tas_droite[0]) / 2.0
27            
28            else: 
29                heapq.heappush(self.tas_gauche, -num)
30                
31                if self.longeur_paire:
32                   
33                    self.mediane = float(-heapq.heappop(self.tas_gauche))
34                else:
35                    
36                    heapq.heappush(self.tas_droite, self.mediane)
37                    
38                    self.mediane = (-self.tas_gauche[0] + self.tas_droite[0]) / 2.0
39
40           
41            self.longeur_paire = not self.longeur_paire
42        
43
44    def findMedian(self):
45        """
46        :rtype: float
47        """
48        return float(self.mediane)
49        
50
51
52# Your MedianFinder object will be instantiated and called as such:
53# obj = MedianFinder()
54# obj.addNum(num)
55# param_2 = obj.findMedian()