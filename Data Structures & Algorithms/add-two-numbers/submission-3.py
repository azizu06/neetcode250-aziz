# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry, dummy = 0, ListNode(0)
        cur = dummy
        while l1 or l2:
            if l1 and l2:
                total = l1.val+l2.val
                if carry > 0: total+=1
                num, carry = total%10, total//10
                newNode = ListNode(num)
                cur.next = newNode
                cur, l1, l2 = cur.next, l1.next, l2.next
            else:
                total = l1.val if l1 else l2.val
                if carry > 0: total+=1
                num, carry = total%10, total//10
                newNode = ListNode(num)
                cur.next = newNode
                cur = cur.next
                if l1:
                    l1 = l1.next
                else:
                    l2 = l2.next
        if carry > 0:
            newNode = ListNode(carry)
            cur.next = newNode
        return dummy.next
