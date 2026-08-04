# Last updated: 04/08/2026 11:37:13
class Solution(object):
    def array_to_dico(self, a): 
        result = {}
        for valeur in a:
            if valeur not in result:
                result[valeur] = 0 
            result[valeur] += 1
        return result
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.array_to_dico(s) == self.array_to_dico(t)