# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        for i in range(len(lists)):
            head = temp = ListNode(0)
            l1, l2 = dummy.next, lists[i]
            while l1 and l2:
                if l1.val <= l2.val:
                    temp.next = l1
                    temp, l1 = temp.next, l1.next
                else:
                    temp.next = l2
                    temp, l2 = temp.next, l2.next
            temp.next = l1 or l2
            dummy.next = head.next
        return dummy.next