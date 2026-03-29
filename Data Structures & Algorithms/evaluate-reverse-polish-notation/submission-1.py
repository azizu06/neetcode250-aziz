class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == '+':
                s.append(s.pop()+s.pop())
            elif t == '-':
                n1 = s.pop()
                n2 = s.pop()
                s.append(n2-n1)
            elif t == '*':
                s.append(s.pop()*s.pop())
            elif t == '/':
                n1 = s.pop()
                n2 = s.pop()
                s.append(int(n2/n1))
            else:
                s.append(int(t))
        return s.pop()