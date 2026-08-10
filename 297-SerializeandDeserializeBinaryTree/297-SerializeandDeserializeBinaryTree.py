# Last updated: 10/08/2026 17:02:13
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7from collections import deque
8
9class Codec:
10
11    def serialize(self, root):
12        """Encodes a tree to a single string.
13        
14        :type root: TreeNode
15        :rtype: str
16        """
17        if not root:
18            return ""
19
20        res = []
21        queue = deque([root])
22        
23        while queue:
24            node = queue.popleft()
25            
26            if node:
27                res.append(str(node.val))
28                queue.append(node.left)
29                queue.append(node.right)
30            else:
31                res.append("n")
32            
33        return ",".join(res)
34
35    def deserialize(self, data):
36        """Decodes your encoded data to tree.
37        
38        :type data: str
39        :rtype: TreeNode
40        """
41        if not data:
42            return None
43            
44        vals = data.split(',')
45        
46        root = TreeNode(int(vals[0]))
47        queue = deque([root])
48        
49        i = 1 
50        
51        while queue:
52            node = queue.popleft()
53            
54            if vals[i] != "n":
55                node.left = TreeNode(int(vals[i]))
56                queue.append(node.left)
57            i += 1
58        
59            if vals[i] != "n":
60                node.right = TreeNode(int(vals[i]))
61                queue.append(node.right)
62            i += 1
63            
64        return root
65
66# Your Codec object will be instantiated and called as such:
67# ser = Codec()
68# deser = Codec()
69# ans = deser.deserialize(ser.serialize(root))