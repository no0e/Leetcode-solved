# Last updated: 04/08/2026 11:38:17
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        A, B = nums1, nums2
        m, n = len(A), len(B)
        total = m + n
        
        
        half = (total + 1) // 2
        
        
        left = 0
        right = m
        
        while left <= right:
            # i = nombre d'éléments pris dans A
            i = (left + right) // 2
            # j = nombre d'éléments pris dans B pour compléter la moitié
            j = half - i
            A_gauche = A[i - 1] if i > 0 else float('-inf')
            A_droite = A[i] if i < m else float('inf')
            
            B_gauche = B[j - 1] if j > 0 else float('-inf')
            B_droite = B[j] if j < n else float('inf')
            
            
            if A_gauche <= B_droite and B_gauche <= A_droite:
                
                if total % 2 != 0:
                    
                    return float(max(A_gauche, B_gauche))
                    
                
                else:
                    
                    max_gauche = max(A_gauche, B_gauche)
                    min_droite = min(A_droite, B_droite)
                    return (max_gauche + min_droite) / 2.0
                    
            elif A_gauche > B_droite:
                
                right = i - 1
            else:
                
                left = i + 1