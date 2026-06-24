# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        snext = slow.next
        prev = slow.next = None
        while snext:
            nextt = snext.next
            snext.next = prev
            prev = snext
            snext = nextt
        
        left, right = head, prev
        while right:
            l_next, r_next = left.next, right.next
            left.next = right
            right.next = l_next
            left, right= l_next, r_next