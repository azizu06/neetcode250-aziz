class MyQueue:

    def __init__(self):
        self.s = []
        self.t = []
        

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        while len(self.s) > 1:
            self.t.append(self.s.pop())
        res = self.s.pop()
        while len(self.t) > 0:
            self.s.append(self.t.pop())
        return res

    def peek(self) -> int:
        while len(self.s) > 1:
            self.t.append(self.s.pop())
        res = self.s[0]
        while len(self.t) > 0:
            self.s.append(self.t.pop())
        return res

    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()