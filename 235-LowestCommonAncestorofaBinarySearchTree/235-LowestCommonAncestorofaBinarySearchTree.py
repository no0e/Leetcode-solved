# Last updated: 08/08/2026 15:24:05
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution(object):
9        
10    def lowestCommonAncestor(self, root, p, q):
11        
12        if not root or root == p or root == q:
13            return root
14
15       
16        gauche = self.lowestCommonAncestor(root.left, p, q)
17        droite = self.lowestCommonAncestor(root.right, p, q)
18
19        if gauche and droite:
20            return root
21
22        return gauche or droite
23       
24
25            