class MyQueue:

    def __init__(self):
        self.s = []
        self.t = []
        

    def push(self, x: int) -> None:
        while len(self.s) > 0:
            self.t.append(self.s.pop())
        self.s.append(x)
        while len(self.t) > 0:
            self.s.append(self.t.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()