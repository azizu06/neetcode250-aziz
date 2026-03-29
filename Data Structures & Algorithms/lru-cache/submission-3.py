class Node:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val, self.key, self.next, self.prev = val, key, next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.sz = capacity
        self.cache = {}
        self.front, self.rear = Node(), Node()
        self.front.next, self.rear.prev = self.rear, self.front

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.rear
        node.prev = self.rear.prev
        self.rear.prev.next = node
        self.rear.prev = node
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.rear
            node.prev = self.rear.prev
            self.rear.prev.next = node
            self.rear.prev = node
            return
        if self.sz <= 0:
            del self.cache[self.front.next.key]
            self.front.next = self.front.next.next
            self.front.next.prev = self.front.next.prev.prev
        newNode = Node(value, key, self.rear, self.rear.prev)
        self.cache[key] = newNode
        self.rear.prev.next = newNode
        self.rear.prev = newNode
        self.sz-=1
        
