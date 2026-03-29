from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size+=1

    def pop(self) -> int:
        finalSize = self.size
        while self.size > 1:
            self.q1.append(self.q1.popleft())
            self.size-=1
        res = self.q1.popleft()
        self.size = finalSize-1
        return res


    def top(self) -> int:
        finalSize = self.size
        while self.size > 1:
            self.q1.append(self.q1.popleft())
            self.size-=1
        res = self.q1.popleft()
        self.q1.append(res)
        self.size = finalSize
        return res

    def empty(self) -> bool:
        return True if len(self.q1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()