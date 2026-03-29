class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.sz = k
        self.front = Node(0)
        self.rear = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        new = Node(value)
        if self.isEmpty():
            self.front.next = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        self.sz-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front.next = self.front.next.next
        if self.isEmpty():
            self.rear = self.front
        self.sz+=1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.front.next is None

    def isFull(self) -> bool:
        return self.sz == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()