class Solution:
    def checkValidString(self, s: str) -> bool:
        opn, star = [],[]
        for i,c in enumerate(s):
            if c == '(':
                opn.append(i)
            elif c == '*':
                star.append(i)
            else:
                if opn:
                    opn.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while opn and star:
            if opn.pop() > star.pop():
                return False
        return True if len(star) >= len(opn) else False
        
