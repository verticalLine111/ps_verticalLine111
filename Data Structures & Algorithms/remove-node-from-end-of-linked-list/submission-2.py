# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        tgt = length - n          # 앞에서 센 삭제 대상 인덱스

        dummy = ListNode(0, head) # head를 붙잡아두는 고정 노드
        prev = dummy
        for _ in range(tgt):      # 삭제 대상 "직전"까지 전진
            prev = prev.next
        prev.next = prev.next.next  # 직전.next를 건너뛰어 끊기
        return dummy.next