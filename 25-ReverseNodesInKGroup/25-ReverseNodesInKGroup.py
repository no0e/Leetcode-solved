# Last updated: 05/08/2026 23:55:21
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        head_final = None
        prev_tail = None  
        current = head
        
        while current:
            debut_de_boucle = current 
            precedent = None
            i = 0
            
            
            while current and i < k:
                temp = current.next
                current.next = precedent
                precedent = current
                current = temp
                i += 1
                
            if i == k:
                if not head_final:
                    head_final = precedent 
                
                if prev_tail:
                    prev_tail.next = precedent 
                
                prev_tail = debut_de_boucle 
            else:
                curr_re = precedent
                prev_re = None
                
                for _ in range(i):
                    temp_re = curr_re.next
                    curr_re.next = prev_re
                    prev_re = curr_re
                    curr_re = temp_re
                    
                if prev_tail:
                    prev_tail.next = prev_re
                
                
                if not head_final:
                    head_final = prev_re
                    
        return head_final