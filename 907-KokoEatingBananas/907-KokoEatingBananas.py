# Last updated: 04/08/2026 11:37:01
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        
       
        res = right 
        
        while left <= right:
            mid = (left + right) // 2 
            h_n = sum((element + mid - 1) // mid for element in piles)
            
            if h_n <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return res