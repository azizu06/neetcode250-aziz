# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: return None
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast: return head.next
        while fast:
            prev = slow
            slow, fast = slow.next, fast.next
        prev.next = prev.next.next
        return head