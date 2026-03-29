# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = fast = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if not fast: return False
            if fast == slow: return True
        return False