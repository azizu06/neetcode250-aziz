class Solution:
    def decodeString(self, s: str) -> str:
        k = []
        stack = []
        num = ""
        cur = ""
        for c in s:
            if c.isdigit():
                num+=c
            elif c == '[':
                k.append(int(num))
                num = ""
                stack.append(cur)
                cur = ""
            elif c == ']':
                inner= k.pop()*cur
                cur = stack.pop()+inner
            else:
                cur+=c
        return cur

