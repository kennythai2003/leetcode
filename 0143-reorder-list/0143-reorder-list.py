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

        curr = slow        
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        l1 = head
        l2 = prev

        while l2 and l2.next:
            temp1 = l1.next
            l1.next = l2 
            l1 = temp1

            temp2 = l2.next
            l2.next = l1
            l2 = temp2
        