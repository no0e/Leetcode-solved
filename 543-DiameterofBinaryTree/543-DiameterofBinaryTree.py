# Last updated: 07/08/2026 10:56:52
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def diameterOfBinaryTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        self.diametre_max = 0 
14
15        def profondeur(noeud):
16            if not noeud:
17                return 0 
18            
19            gauche = profondeur(noeud.left)
20            droite = profondeur(noeud.right)
21            
22            self.diametre_max = max(self.diametre_max, gauche + droite)
23            
24            return 1 + max(gauche, droite)
25        
26    
27        profondeur(root)
28        
29        return self.diametre_max