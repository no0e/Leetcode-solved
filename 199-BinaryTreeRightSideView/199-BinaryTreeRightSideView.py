# Last updated: 08/08/2026 16:12:27
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def rightSideView(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: List[int]
12        """
13        
14        #parcours BFS , renvoyez le dernier de chaque étage
15
16        if not root: 
17            return []
18        res = []
19
20        queue = [root]
21
22        while queue:
23                
24            level_size = len(queue)
25            current_level = []
26            
27            for _ in range(level_size):
28                curr = queue.pop(0) 
29                current_level.append(curr.val) 
30                
31                if curr.left:
32                    queue.append(curr.left)
33                if curr.right:
34                    queue.append(curr.right)
35            
36            
37            res.append(current_level[-1])
38
39        return res
40