# Last updated: 06/08/2026 10:09:51
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x, next=None, random=None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution(object):
11    def copyRandomList(self, head):
12        if not head:
13            return None
14            
15        #Doubler les nœuds
16        curr = head
17        while curr:
18            clone = Node(curr.val, curr.next)
19            curr.next = clone
20            curr = clone.next
21            
22        #Copier les pointeurs random
23        curr = head
24        while curr:
25            if curr.random:
26                curr.next.random = curr.random.next
27            curr = curr.next.next
28            
29        #Séparer les deux listes
30        curr = head
31        cloned_head = head.next 
32        
33        while curr:
34            clone = curr.next
35            curr.next = clone.next
36            
37            if clone.next:
38                clone.next = clone.next.next
39                
40            curr = curr.next
41            
42        return cloned_head