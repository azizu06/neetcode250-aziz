class Node:
    def __init__(self, key=-1, val=-1, freq=0):
        self.prev = self.next = None
        self.key, self.val, self.freq = key, val, freq

class Dll:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
        
class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.freq = {1: Dll()}
        self.cap = capacity
        self.sz = 0
        self.sm = 1

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        dll = self.freq[node.freq]
        node.freq+=1
        if dll.head.next == dll.tail: self.sm = node.freq
        if node.freq not in self.freq: self.freq[node.freq] = Dll()
        dll = self.freq[node.freq]
        self.add(node, dll)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            dll = self.freq[node.freq]
            self.remove(node)
            node.freq+=1
            if dll.head.next == dll.tail: self.sm = node.freq
            if node.freq not in self.freq: self.freq[node.freq] = Dll()
            dll = self.freq[node.freq]
            self.add(node, dll)
            return
        if self.sz >= self.cap:
            dll = self.freq[self.sm]
            node = dll.tail.prev
            del self.cache[node.key]
            self.remove(node)
            if dll.head.next == dll.tail: self.sm = node.freq+1
            self.sz-=1
        node = Node(key, value, 1)
        self.cache[key] = node
        self.sm = node.freq
        dll = self.freq[node.freq]
        self.add(node, dll)
        self.sz+=1
        
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