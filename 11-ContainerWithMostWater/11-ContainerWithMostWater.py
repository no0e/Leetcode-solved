# Last updated: 04/08/2026 11:38:12
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n= len(height)
        g ,d  = 0 , n-1
        aire_max=0
        
        while g<d : 
            aire =min(height[g],height[d])*(d-g)
            if aire > aire_max :
                aire_max = aire
                g_max = g
                d_max = d 
            if height[g] > height[d] :
                d -= 1
            else:
                g+=1
        
            
        return aire_max


        