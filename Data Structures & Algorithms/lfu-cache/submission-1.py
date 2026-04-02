class Node:
    def __init__(self, key=-1, val=-1, freq=0):
        self.prev = self.next = None
        self.key, self.val, self.freq = key, val, freq

class Dll:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    def empty(self):
        return self.head.next == self.tail
        
class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = defaultdict(Dll)
        self.cap = capacity
        self.sm = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.move(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move(node)
            return
        if self.cap == len(self.cache):
            dll = self.freq[self.sm]
            node = dll.tail.prev
            del self.cache[node.key]
            self.remove(node)
        node = Node(key, value, 1)
        self.cache[key] = node
        self.sm = 1
        self.add(node, self.freq[node.freq])

    def move(self, node):
        dll = self.freq[node.freq]
        self.remove(node)
        if node.freq == self.sm and dll.empty(): self.sm+=1
        node.freq+=1
        self.add(node, self.freq[node.freq])

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def add(self, node, dll):
        node.next, node.prev = dll.head.next, dll.head
        node.next.prev = dll.head.next = node
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)