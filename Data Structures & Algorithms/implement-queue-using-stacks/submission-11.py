class MyQueue:

    def __init__(self):
        self.s = []
        self.t = []
        

    def push(self, x: int) -> None:
        self.s.append(x)


    def pop(self) -> int:
        if len(self.t) != 0:
            return self.t.pop()
        while len(self.s) > 0:
            self.t.append(self.s.pop())
        return self.t.pop()



    def peek(self) -> int:
        if len(self.t) != 0:
            return self.t[-1]
        while len(self.s) > 0:
            self.t.append(self.s.pop())
        return self.t[-1]
        

    def empty(self) -> bool:
        return len(self.s) == 0 and len(self.t) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()