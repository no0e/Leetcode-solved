# Last updated: 05/08/2026 23:55:11
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict() 

    def get(self, key):
        if key not in self.dict:
            return -1
        
        valeur = self.dict.pop(key)
        self.dict[key] = valeur
        return valeur

    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        elif len(self.dict) == self.capacity:
            premiere_cle = next(iter(self.dict))
            self.dict.pop(premiere_cle)
        
        self.dict[key] = value