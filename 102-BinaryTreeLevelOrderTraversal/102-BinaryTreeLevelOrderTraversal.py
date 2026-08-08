# Last updated: 08/08/2026 15:53:03
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def levelOrder(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: List[List[int]]
12        """
13        if not root: 
14            return []
15            
16        res = []
17        queue = [root]
18        
19        while queue:
20            level_size = len(queue)
21            current_level = []
22            
23            for _ in range(level_size):
24                curr = queue.pop(0) 
25                current_level.append(curr.val) 
26                
27                
28                if curr.left:
29                    queue.append(curr.left)
30                if curr.right:
31                    queue.append(curr.right)
32            
33           
34            res.append(current_level)
35            
36        return res