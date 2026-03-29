class MinStack:

    def __init__(self):
        self.s = []
        self.m = []
        self.small = None

    def push(self, val: int) -> None:
        if self.small is None or val <= self.small:
            self.small = val
            self.s.append(val)
            self.m.append(val)
        else:
            self.s.append(val)

    def pop(self) -> None:
        if self.s[-1] == self.m[-1]:
            self.m.pop()
            if self.m:
                self.small = self.m[-1]
            else:
                self.small = None
        return self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
