from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        size = len(self.q)
        while size > 1:
            self.q.append(self.q.popleft())
            size-=1
        res = self.q.popleft()
        return res


    def top(self) -> int:
        size = len(self.q)
        while size > 1:
            self.q.append(self.q.popleft())
            size-=1
        res = self.q.popleft()
        self.q.append(res)
        return res

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()