# Last updated: 04/08/2026 11:37:55
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        

        n = len(matrix)
        
        milieu = n//2
        right = n-1
        left = 0

        while left <= right:
            if target == matrix[milieu][0]:
                return True
            if target > matrix[milieu][0]:
                left = milieu +1
            if target < matrix[milieu][0]:
                right = milieu -1
            milieu = (right+left)//2
        
        
        m = len(matrix[milieu])
        
        milieu2 = m//2
        right = m-1
        left = 0
        while left <= right:
            if target == matrix[milieu][milieu2]:
                return True
            if target > matrix[milieu][milieu2]:
                left = milieu2 +1
            if target < matrix[milieu][milieu2]:
                right = milieu2 -1
            milieu2 = (right+left)//2
        return False