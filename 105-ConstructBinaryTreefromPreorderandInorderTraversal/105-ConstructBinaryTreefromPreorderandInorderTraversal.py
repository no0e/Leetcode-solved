# Last updated: 09/08/2026 14:32:39
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def buildTree(self, preorder, inorder):
9        """
10        :type preorder: List[int]
11        :type inorder: List[int]
12        :rtype: Optional[TreeNode]
13        """
14        if not preorder or not inorder:
15            return None
16
17        valeur_racine = preorder[0]
18        racine = TreeNode(valeur_racine)
19
20        mid = inorder.index(valeur_racine)
21
22        inorder_gauche = inorder[:mid]
23        inorder_droite = inorder[mid + 1:]
24        
25        #Dans le préfixe, on prend les mid éléments juste après la racine pour la gauche
26        preorder_gauche = preorder[1:mid + 1]
27        preorder_droite = preorder[mid + 1:]
28
29        racine.left = self.buildTree(preorder_gauche, inorder_gauche)
30        racine.right = self.buildTree(preorder_droite, inorder_droite)
31
32        return racine