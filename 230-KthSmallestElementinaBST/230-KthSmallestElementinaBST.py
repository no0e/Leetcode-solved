# Last updated: 09/08/2026 13:43:22
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def kthSmallest(self, root, k):
9        """
10        :type root: Optional[TreeNode]
11        :type k: int
12        :rtype: int
13        """
14        
15        #on fait un parcours en profondeur ,jusqua arriver à une feuille , en prend ensuite les k premier du parcours
16
17        def DFS(root):
18            if not root:
19                return []   
20            
21            
22            
23            gauche = DFS(root.left)
24            droite = DFS(root.right)
25
26
27            return gauche + [root.val] + droite
28
29        tab = DFS(root)
30        return tab[k-1]
31    
32
33            
34