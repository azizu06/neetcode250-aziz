from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.q2.append(x)
        self.size+=1

    def pop(self) -> int:
        while len(self.q2) > 1:
            self.q2.popleft()
        res = self.q2.popleft()
        self.size-=1
        for i in range(self.size):
            self.q2.append(self.q1[i])
        return res


    def top(self) -> int:
        while len(self.q2) > 1:
            self.q2.popleft()
        res = self.q2[0]
        for i in range(self.size):
            self.q2.append(self.q1[i])
        return res


    def empty(self) -> bool:
        if len(self.q2) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()