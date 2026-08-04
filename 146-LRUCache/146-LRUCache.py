# Last updated: 04/08/2026 15:15:27
1from collections import OrderedDict
2
3class LRUCache(object):
4
5    def __init__(self, capacity):
6        self.capacity = capacity
7        self.dict = OrderedDict() 
8
9    def get(self, key):
10        if key not in self.dict:
11            return -1
12        
13        valeur = self.dict.pop(key)
14        self.dict[key] = valeur
15        return valeur
16
17    def put(self, key, value):
18        if key in self.dict:
19            self.dict.pop(key)
20        elif len(self.dict) == self.capacity:
21            premiere_cle = next(iter(self.dict))
22            self.dict.pop(premiere_cle)
23        
24        self.dict[key] = value