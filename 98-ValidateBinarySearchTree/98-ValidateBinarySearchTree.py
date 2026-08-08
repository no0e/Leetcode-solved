# Last updated: 08/08/2026 18:22:49
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution(object):
9    def isValidBST(self, root):
10        """
11        :type root: Optional[TreeNode]
12        :rtype: bool
13        """
14        def dfs(noeud, min_val, max_val):
15            
16            if not noeud:
17                return True
18            
19            if noeud.val <= min_val or noeud.val >= max_val:
20                return False
21            
22            return dfs(noeud.left, min_val, noeud.val) and dfs(noeud.right, noeud.val, max_val)
23
24        return dfs(root, float('-inf'), float('inf'))