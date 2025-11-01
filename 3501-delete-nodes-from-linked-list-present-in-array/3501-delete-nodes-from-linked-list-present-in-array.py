# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numsmap = {}
        for n in nums:
            numsmap[n] = 1 + numsmap.get(n, 0)
        
        dummy = ListNode(0, head)
        prev = dummy

        curr = head
        while curr:
            if curr.val in numsmap:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
        
        return dummy.next