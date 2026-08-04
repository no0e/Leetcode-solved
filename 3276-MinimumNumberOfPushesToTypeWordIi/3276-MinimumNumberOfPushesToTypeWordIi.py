# Last updated: 04/08/2026 11:36:57
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """

        compteur = Counter(word)
        n = len(compteur)
        multiple_de_huit = 1
        dans_la_huitaine = 0
        result = 0
        for lettre, frequence in compteur.most_common():
            if dans_la_huitaine <8:
                
                dans_la_huitaine += 1
            else:
                dans_la_huitaine = 1
                multiple_de_huit +=1 

            result += multiple_de_huit*frequence

        return result



