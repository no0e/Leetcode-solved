# Last updated: 04/08/2026 11:37:11
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
       
        return [element for element, frequence in Counter(nums).most_common(k)]
               
            
        