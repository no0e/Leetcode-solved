# Last updated: 04/08/2026 11:36:59
class TimeMap(object):

    def __init__(self):
        self.dict = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        # OPTIMISATION : On utilise append() plutôt que la concaténation de listes
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = "" # Valeur par défaut si on ne trouve rien
        
        # Si la clé n'existe pas du tout, on s'arrête direct
        if key not in self.dict:
            return res
            
        valeurs = self.dict[key]
        left = 0
        right = len(valeurs) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            
            mid_timestamp = valeurs[mid][1]
            
            if mid_timestamp == timestamp:
                
                return valeurs[mid][0]
                
            elif mid_timestamp < timestamp:
                res = valeurs[mid][0]
                left = mid + 1
                
            else:
                right = mid - 1
                
        return res