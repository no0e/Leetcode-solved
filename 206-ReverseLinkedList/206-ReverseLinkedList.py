# Last updated: 04/08/2026 11:37:23
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        precedent = None
        current = head

        while current != None :
            prochain = current.next
            current.next = precedent
            precedent = current
            current = prochain
        return precedent           
            
        