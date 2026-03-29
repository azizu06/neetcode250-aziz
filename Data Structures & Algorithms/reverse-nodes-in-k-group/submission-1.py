# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = r = dummy
        for _ in range(k):
            if not r: return dummy.next
            r = r.next
        while r:
            prev, cur = None, l.next
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp2 = l.next
            l.next.next = cur
            l.next = prev
            l = r = temp2
            for _ in range(k):
                if not r: return dummy.next
                r = r.next
        return dummy.next