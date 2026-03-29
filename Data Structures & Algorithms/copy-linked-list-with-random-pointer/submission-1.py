"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curOld, curNew = head, dummy
        rnd = {None: None}
        while curOld:
            newNode = Node(curOld.val)
            curNew.next = newNode
            curNew = curNew.next
            rnd[curOld] = curNew
            curOld = curOld.next
        curOld, curNew = head, dummy.next
        while curNew:
            curNew.random = rnd[curOld.random]
            curNew, curOld = curNew.next, curOld.next
        return dummy.next


