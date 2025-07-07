# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversedl = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = reversedl
            reversedl = curr
            curr = temp
        
        firstl = head
        secondl = reversedl 
        
        while secondl.next:
           temp1 = firstl.next
           firstl.next = secondl
           firstl = temp1

           temp2 = secondl.next
           secondl.next = firstl
           secondl = temp2
        