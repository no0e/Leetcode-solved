# Last updated: 08/08/2026 16:46:09
1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode(object):
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution(object):
9    def goodNodes(self, root):
10        if not root: 
11            return 0
12            
13        compteur_bons_noeuds = 0
14        
15        queue = deque([(root, root.val)])
16        
17        while queue:
18            curr, max_so_far = queue.popleft() 
19            
20            if curr.val >= max_so_far:
21                compteur_bons_noeuds += 1
22            
23            nouveau_max = max(max_so_far, curr.val)
24            
25            
26            if curr.left:
27                queue.append((curr.left, nouveau_max))
28            if curr.right:
29                queue.append((curr.right, nouveau_max))
30                
31        return compteur_bons_noeuds