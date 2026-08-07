# Last updated: 07/08/2026 11:36:49
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSubtree(self, root, subRoot):
9        """
10        :type root: Optional[TreeNode]
11        :type subRoot: Optional[TreeNode]
12        :rtype: bool
13        """
14        if not root:
15            return False
16
17        if self.isSameTree(root, subRoot):
18            return True
19            
20        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
21
22    def isSameTree(self, p, q):
23        if not p and not q:
24            return True
25        
26        if not p or not q:
27            return False
28            
29        if p.val != q.val:
30            return False
31            
32        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)