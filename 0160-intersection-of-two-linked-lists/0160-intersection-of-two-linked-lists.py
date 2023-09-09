# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        list1 = headA
        list2 = headB

        while list1 != list2:
            if list1 is None:
                list1= headB
            else:
                list1 = list1.next
            
            if list2 is None:
                list2 = headA
            else:
                list2 = list2.next
        
        return list1