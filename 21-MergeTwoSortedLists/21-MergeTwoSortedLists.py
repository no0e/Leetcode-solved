# Last updated: 04/08/2026 11:38:07
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode()
        current = temp
        while (list1 is not None) and (list2 is not None) :
            valeur1 = list1.val
            valeur2 = list2.val
            if valeur1 <= valeur2:
                current.next = list1
                list1 = list1.next

            
            else :
                current.next = list2
                list2 = list2.next

            current = current.next

            
        if list1 is None:
            current.next = list2

        else:
            current.next = list1
        return temp.next
        
        