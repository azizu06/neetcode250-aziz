# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lprev, cur = dummy, head
        for _ in range(left-1):
            lprev, cur = lprev.next, cur.next
        prev = None
        for _ in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        lprev.next.next = cur
        lprev.next = prev
        
        return dummy.next

        