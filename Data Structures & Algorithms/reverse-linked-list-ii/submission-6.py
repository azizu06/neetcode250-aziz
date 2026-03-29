# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        l = r = head
        pre = None
        for i in range(right-1):
            if i < left-1:
                pre = l
                l = l.next
            r = r.next
        post = r.next
        prev, cur = None, l
        while cur != post:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        l.next = post
        if pre: 
            pre.next = r
            return head
        return r

        