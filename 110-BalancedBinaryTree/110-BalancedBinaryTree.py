# Last updated: 07/08/2026 11:13:12
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        #on regarde si droite et gauche on un ecrat de  ou  recursivment
14        self.balanced = True
15        def profondeur(noeud):
16            if not noeud:
17                return 0
18            gauche = profondeur(noeud.left)
19            droite = profondeur(noeud.right)
20
21            if self.balanced and abs(gauche - droite) >1:
22                self.balanced = False
23               
24
25            return 1 + max(gauche,droite)
26        profondeur(root)
27
28        return self.balanced