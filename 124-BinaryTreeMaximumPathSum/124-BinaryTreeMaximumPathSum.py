# Last updated: 09/08/2026 15:51:27
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def __init__(self):
9        self.max_global = float('-inf')
10
11    def maxPathSum(self, root):
12        """
13        :type root: Optional[TreeNode]
14        :rtype: int
15        """
16
17        def DFS(node):
18            if not node:
19                return 0
20            
21            gauche = max(DFS(node.left), 0)
22            droite = max(DFS(node.right), 0)
23            
24            somme_pont = node.val + gauche + droite
25            
26            self.max_global = max(self.max_global, somme_pont)
27            
28            return node.val + max(gauche, droite)
29
30        DFS(root)
31        
32        return self.max_global