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
        cutt = slow.next
        slow.next = None
        prev = None
        while cutt:
            nextt = cutt.next
            cutt.next = prev
            prev = cutt
            cutt = nextt
        right,left = head, prev
        while left:
            n_right, n_left = right.next, left.next
            right.next = left
            left.next = n_right
            right,left = n_right, n_left            