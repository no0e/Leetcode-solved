# Last updated: 04/08/2026 11:37:27
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dico = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dico:
                return [dico[target - numbers[i]]+1,i+1]
            else : 
                dico[numbers[i]] = i
                
        