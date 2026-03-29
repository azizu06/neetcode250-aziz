class Node:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val, self.key, self.next, self.prev = val, key, next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.sz = capacity
        self.cache = {}
        self.front, self.rear = Node(), Node()
        self.front.next, self.rear.prev = self.rear, self.front
    
    def removeInsert(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next, node.prev = self.rear, self.rear.prev
        self.rear.prev.next = self.rear.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.removeInsert(self.cache[key])
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeInsert(self.cache[key])
            self.cache[key].val = value
            return
        if len(self.cache) >= self.sz:
            node = self.cache[self.front.next.key]
            del self.cache[self.front.next.key]
            self.front.next, node.next.prev = node.next, self.front
        newNode = Node(value, key, self.rear, self.rear.prev)
        self.cache[key] = newNode
        self.rear.prev.next = self.rear.prev = newNode
        
