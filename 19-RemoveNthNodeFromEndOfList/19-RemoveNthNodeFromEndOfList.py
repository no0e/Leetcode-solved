# Last updated: 04/08/2026 11:38:09
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        #reverse
        dummy = ListNode()
        dummy.next = head

        lent = dummy
        rapide = dummy
        
        for i in range(n+1):
            rapide = rapide.next

        while rapide is not None:
            lent = lent.next
            rapide = rapide.next

        lent.next = lent.next.next

        return dummy.next
