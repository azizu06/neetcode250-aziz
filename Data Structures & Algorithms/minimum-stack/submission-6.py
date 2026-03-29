class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.m and val > self.m[-1]:
            mini = self.m[-1]
        else:
            mini = val
        self.m.append(mini)


    def pop(self) -> None:
        self.m.pop()
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
