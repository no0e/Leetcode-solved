# Last updated: 04/08/2026 11:38:21
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        retenue = 0
        dummy = ListNode(0)
        curr = dummy
       
        while l1 or l2 or retenue:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            somme = retenue + v1 + v2
            retenue = somme // 10
            somme = somme % 10

            curr.next = ListNode(somme)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        

        return dummy.next
            
        