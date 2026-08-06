# Last updated: 06/08/2026 10:38:45
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def invertTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: Optional[TreeNode]
12        """
13        if not root:
14            return None
15        
16        root.left, root.right = root.right, root.left
17
18        self.invertTree(root.left)
19        
20        self.invertTree(root.right)
21
22        return root
23   