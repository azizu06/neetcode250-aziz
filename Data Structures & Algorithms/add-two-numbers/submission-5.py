# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, dummy = 0, ListNode(0)
        cur = dummy
        while l1 or l2 or carry:
            total = carry+(l1.val if l1 else 0)+(l2.val if l2 else 0)
            num, carry = total%10, total//10
            newNode = ListNode(num)
            cur.next = newNode
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            cur = cur.next
        return dummy.next
