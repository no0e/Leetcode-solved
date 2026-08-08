# Last updated: 08/08/2026 15:20:31
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution(object):
9    
10    def contient_noeud(self, root, cible):
11        if not root:
12            return False
13        if cible == root:
14            return True
15        
16        
17        gauche = self.contient_noeud(root.left, cible)
18        droite = self.contient_noeud(root.right, cible)
19
20        return gauche or droite
21        
22    def lowestCommonAncestor(self, root, p, q):
23        
24        if not root or root == p or root == q:
25            return root
26
27       
28        p_gauche = self.contient_noeud(root.left, p)
29        q_gauche = self.contient_noeud(root.left, q)
30
31        if p_gauche != q_gauche:
32            return root
33        else:
34            if p_gauche:
35                
36                return self.lowestCommonAncestor(root.left, p, q)
37            else: 
38                
39                return self.lowestCommonAncestor(root.right, p, q)