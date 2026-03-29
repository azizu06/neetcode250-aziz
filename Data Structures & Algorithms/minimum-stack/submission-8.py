class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        if not self.m or val <= self.m[-1]:
            self.s.append(val)
            self.m.append(val)
        else:
            self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.m[-1]:
            self.m.pop()
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
