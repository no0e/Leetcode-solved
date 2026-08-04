# Last updated: 04/08/2026 11:37:50
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [] #stack d'indices
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                index_courant = stack.pop()
                if stack:
                    left = stack[-1]
                    largeur = i - left - 1
                else:
                     largeur = i
                
                max_area = max(max_area, heights[index_courant] * largeur)
        
            stack.append(i)

        return max_area